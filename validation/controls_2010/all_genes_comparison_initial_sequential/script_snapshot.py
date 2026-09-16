"""Compare deposited Kertesz 2010 PARS measurements with rnavail predictions.

No work happens on import. See ALL_GENES.md for inputs, options and interpretation.
"""
from __future__ import annotations

import argparse
from array import array
from bisect import bisect_left, bisect_right
from collections import Counter, defaultdict
import csv
from datetime import datetime, timezone
import gzip
import hashlib
import json
import math
from pathlib import Path
import statistics
import sys
import time

REPO = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO))
SCRIPT_VERSION = '1'
ROMAN = 'I II III IV V VI VII VIII IX X XI XII XIII XIV XV XVI'.split()
SOURCE_FILES = {
    'transcripts': 'GSE22393_sce_genes.fasta.gz',
    'genome': 'GSE22393_sce_0608.fasta.gz',
    'annotation': 'GSE22393_sce_transcriptome_global.tab.gz',
    'pars': 'GSE22393_processed_merged_PARS_sacCer2_1.wig.gz',
}
ALLOWED_TOOLS = {'rnaplfold', 'rnafold', 'rnastructure-partition', 'contrafold', 'eternafold'}
WINDOW_COLUMNS = ['start','end','n_measured','mean_pars','full_p',
    'seed_start','seed_end','seed_p','seed_n_measured','seed_mean_pars']


def dump_json(path, value):
    """Atomic checkpoints; never emit nonstandard JSON NaN/Infinity."""
    temporary = path.with_suffix(path.suffix+'.tmp')
    temporary.write_text(json.dumps(value, indent=2, allow_nan=False)+'\n')
    temporary.replace(path)


def sha256(path):
    digest = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024*1024), b''):
            digest.update(chunk)
    return digest.hexdigest()


def read_fasta(path):
    records = {}
    name = None
    with gzip.open(path, 'rt') as stream:
        for line in stream:
            line = line.strip()
            if not line:
                continue
            if line.startswith('>'):
                name = line[1:].split()[0]
                if name in records:
                    raise ValueError(f'Duplicate FASTA record: {name}')
                records[name] = []
            elif name is None:
                raise ValueError(f'Sequence before FASTA header: {path}')
            else:
                records[name].append(line.upper())
    if not records or any(not chunks for chunks in records.values()):
        raise ValueError(f'Empty FASTA input/record: {path}')
    return {name: ''.join(chunks) for name, chunks in records.items()}


def read_annotation(path):
    mapping = {}
    with gzip.open(path, 'rt') as stream:
        for line in stream:
            name, chrom, start, end, feature = line.rstrip().split('\t')
            if feature != 'Transcript':
                continue
            if name in mapping:
                raise ValueError(f'Duplicate Transcript annotation: {name}')
            if chrom not in {str(i) for i in range(1,17)}:
                raise ValueError(f'Unsupported chromosome: {chrom}')
            start, end = int(start), int(end)
            if min(start,end) < 1:
                raise ValueError('Annotation must be one-based inclusive')
            mapping[name] = (chrom, start, end)
    return mapping


def read_wig(path):
    """Sparse chromosome arrays, avoiding a Python object for every genomic base."""
    positions, scores = {}, {}
    chrom = None
    with gzip.open(path, 'rt') as stream:
        for number, line in enumerate(stream, 1):
            line = line.strip()
            if not line or line.startswith(('#','browser','track')):
                continue
            if line.startswith('variableStep'):
                fields = dict(part.split('=',1) for part in line.split()[1:])
                if int(fields.get('span','1')) != 1:
                    raise ValueError('Only single-nucleotide WIG span=1 is supported')
                chrom = fields['chrom']
                positions.setdefault(chrom, array('I'))
                scores.setdefault(chrom, array('d'))
                continue
            if line.startswith('fixedStep') or chrom is None:
                raise ValueError(f'Expected variableStep WIG at line {number}')
            coordinate, score = line.split()
            coordinate, score = int(coordinate), float(score)
            if coordinate < 1 or not math.isfinite(score):
                raise ValueError(f'Invalid WIG value at line {number}')
            if positions[chrom] and coordinate <= positions[chrom][-1]:
                raise ValueError(f'Duplicate/out-of-order WIG coordinate at line {number}')
            positions[chrom].append(coordinate)
            scores[chrom].append(score)
    if not positions:
        raise ValueError('No PARS values found')
    return positions, scores


def validate_mapping(sequence, location, genome):
    chrom, start, end = location
    segment = genome[chrom][min(start,end)-1:max(start,end)]
    if start > end:
        segment = segment.translate(str.maketrans('ACGT','TGCA'))[::-1]
    if segment.replace('T','U') != sequence.upper().replace('T','U'):
        raise ValueError('Deposited transcript does not equal its annotated genomic interval; no guessed alignment or intron correction applied')


def map_measurements(location, wig, opposite_intervals=(), exclude_antisense=True):
    chrom, start, end = location
    coordinates, values = wig
    chrom = 'chr'+ROMAN[int(chrom)-1]
    coordinates, values = coordinates.get(chrom,()), values.get(chrom,())
    direction = 1 if start <= end else -1
    lo, hi = min(start,end), max(start,end)
    ambiguous = set()
    for other_lo, other_hi in opposite_intervals:
        for coordinate in range(max(lo,other_lo),min(hi,other_hi)+1):
            ambiguous.add(coordinate)
    pars = {}
    n_ambiguous_measured = 0
    for index in range(bisect_left(coordinates,lo),bisect_right(coordinates,hi)):
        coordinate = coordinates[index]
        if coordinate in ambiguous:
            n_ambiguous_measured += 1
            if exclude_antisense:
                continue
        pars[(coordinate-start)*direction+1] = values[index]
    return pars, n_ambiguous_measured


class Moments:
    """Stable online/mergeable Pearson moments; pooled arrays are unnecessary."""
    def __init__(self, state=None):
        self.state = dict(state or {'n':0,'mx':0.,'my':0.,'xx':0.,'yy':0.,'xy':0.})

    def add(self, x, y):
        s = self.state
        n = s['n']+1
        dx, dy = x-s['mx'], y-s['my']
        s['mx'] += dx/n
        s['my'] += dy/n
        s['xx'] += dx*(x-s['mx'])
        s['yy'] += dy*(y-s['my'])
        s['xy'] += dx*(y-s['my'])
        s['n'] = n

    def merge(self, other):
        a, b = self.state, other.state
        if not b['n']:
            return
        if not a['n']:
            self.state = dict(b)
            return
        n = a['n']+b['n']
        dx,dy = b['mx']-a['mx'], b['my']-a['my']
        weight = a['n']*b['n']/n
        a['xx'] += b['xx']+dx*dx*weight
        a['yy'] += b['yy']+dy*dy*weight
        a['xy'] += b['xy']+dx*dy*weight
        a['mx'] += dx*b['n']/n
        a['my'] += dy*b['n']/n
        a['n'] = n

    def correlation(self):
        s = self.state
        if s['n'] < 3 or s['xx'] <= 0 or s['yy'] <= 0:
            return None
        return max(-1.,min(1.,s['xy']/math.sqrt(s['xx']*s['yy'])))


def ranks(values):
    result = [0.] * len(values)
    order = sorted(range(len(values)),key=values.__getitem__)
    i = 0
    while i < len(order):
        j = i+1
        while j < len(order) and values[order[j]] == values[order[i]]:
            j += 1
        for index in order[i:j]:
            result[index] = (i+j-1)/2
        i = j
    return result


def correlation_stats(x, y, min_pairs):
    if len(x) != len(y):
        raise ValueError('Unmatched comparison arrays')
    moments = Moments()
    for a,b in zip(x,y):
        if not math.isfinite(a) or not math.isfinite(b):
            raise ValueError('Nonfinite correlation input')
        moments.add(a,b)
    ranked = Moments()
    if len(x) >= min_pairs:
        for a,b in zip(ranks(x),ranks(y)):
            ranked.add(a,b)
    return {'n_pairs':len(x),
        'pearson':moments.correlation() if len(x)>=min_pairs else None,
        'spearman':ranked.correlation(), 'moments':moments.state}


def window_records(sequence, pars, table, footprint, seed_length, step, min_coverage):
    """All fixed-grid windows, not a shortlist selected on model or experiment."""
    from rnavail.adapters import _vienna as V
    from rnavail.core.sequence import Region
    for start in range(1,len(sequence)-footprint+2,step):
        end = start+footprint-1
        observed = [pars[p] for p in range(start,end+1) if p in pars]
        if len(observed)/footprint < min_coverage:
            continue
        full = V.region_probability_from_table(table,Region(start,end))
        # Require every placement to be tabulated before claiming a best seed.
        seeds = [(s,V.region_probability_from_table(table,Region(s,s+seed_length-1)))
                 for s in range(start,end-seed_length+2)]
        if full is None or any(p is None for _,p in seeds):
            continue
        seed_start, seed_p = max(seeds,key=lambda pair:pair[1])
        seed_observed = [pars[p] for p in range(seed_start,seed_start+seed_length) if p in pars]
        yield {'start':start,'end':end,'n_measured':len(observed),
            'mean_pars':statistics.mean(observed),'full_p':full,
            'seed_start':seed_start,'seed_end':seed_start+seed_length-1,'seed_p':seed_p,
            'seed_n_measured':len(seed_observed),
            'seed_mean_pars':statistics.mean(seed_observed) if seed_observed else None}


def summarize_models(models, min_pairs):
    summaries = {}
    for key, entries in models.items():
        pooled = Moments()
        for entry in entries:
            pooled.merge(Moments(entry['moments']))
        rs = [e['pearson'] for e in entries if e['pearson'] is not None]
        rhos = [e['spearman'] for e in entries if e['spearman'] is not None]
        summaries[key] = {'genes_with_pairs':len(entries), 'genes_with_defined_correlation':len(rs),
            'n_pairs':pooled.state['n'],
            'pooled_pearson':pooled.correlation() if pooled.state['n']>=min_pairs else None,
            'median_gene_pearson':statistics.median(rs) if rs else None,
            'median_gene_spearman':statistics.median(rhos) if rhos else None,
            'fraction_genes_positive_pearson':sum(r>0 for r in rs)/len(rs) if rs else None}
    return summaries


def parser():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source-dir',type=Path,default=Path(__file__).parent/'source')
    p.add_argument('--output-dir',type=Path,default=Path(__file__).parent/'all_genes_comparison')
    p.add_argument('--tools',default='rnaplfold,rnafold',help='Per-base models; optional rnastructure-partition,contrafold,eternafold')
    p.add_argument('--temperature',type=float,default=37.)
    p.add_argument('--window-size',type=int,default=200)
    p.add_argument('--max-bp-span',type=int,default=150)
    p.add_argument('--local-scope',choices=['bounded','full'],default='bounded')
    p.add_argument('--footprint',type=int,default=20)
    p.add_argument('--seed-length',type=int,default=8)
    p.add_argument('--step',type=int,default=1)
    p.add_argument('--min-pairs',type=int,default=20)
    p.add_argument('--min-window-coverage',type=float,default=.8)
    p.add_argument('--max-length',type=int,help='Optional length ceiling, explicitly recorded as skipped')
    p.add_argument('--gene',action='append',help='Optional exact transcript ID; repeatable. Default is all deposited records.')
    p.add_argument('--keep-antisense-overlaps',action='store_true')
    p.add_argument('--details',action='store_true',help='Write compressed per-base and per-window data for each gene')
    p.add_argument('--resume',action='store_true')
    p.add_argument('--retry-failed',action='store_true',help='With --resume, recompute checkpoints with failed models')
    return p


def main(argv=None):
    p = parser()
    args = p.parse_args(argv)
    tools = list(dict.fromkeys(t.strip() for t in args.tools.split(',') if t.strip()))
    if not tools or set(tools)-ALLOWED_TOOLS:
        p.error('Use only: '+','.join(sorted(ALLOWED_TOOLS)))
    if not 1<=args.seed_length<=args.footprint or args.step<1 or args.min_pairs<3:
        p.error('Require 1 <= seed <= footprint, step >= 1 and min-pairs >= 3')
    if not 0<args.min_window_coverage<=1 or args.max_bp_span<1 or args.window_size<args.max_bp_span:
        p.error('Require coverage in (0,1] and 1 <= max-bp-span <= window-size')
    if args.local_scope=='bounded' and args.window_size<args.footprint:
        p.error('Local window must accommodate the full footprint')
    if not math.isfinite(args.temperature) or args.temperature<=-273.15:
        p.error('Temperature must be finite and above absolute zero')
    if args.max_length is not None and args.max_length<1:
        p.error('max-length must be positive')
    if args.retry_failed and not args.resume:
        p.error('retry-failed requires resume')

    from rnavail.adapters.registry import get
    from rnavail.adapters.base import AccessibilityRequest
    from rnavail.adapters import _vienna as V
    from rnavail.core.sequence import Sequence, Region
    from rnavail.core.model import ModelSettings, RecognitionSpec

    sources = {k:args.source_dir/f for k,f in SOURCE_FILES.items()}
    for path in sources.values():
        if not path.is_file():
            p.error(f'Missing source file: {path}; use the previously downloaded GSE22393 files')
    source_manifest = {k:{'filename':v.name,'sha256':sha256(v)} for k,v in sources.items()}
    adapters = {name:get(name) for name in tools if name!='rnaplfold'}
    inventory = {}
    for name,adapter in adapters.items():
        availability = adapter.availability()
        inventory[name] = {'available':availability.available,'version':availability.version}
    if 'rnaplfold' in tools:
        availability = V.availability()
        inventory['rnaplfold'] = {'available':availability.available,'version':availability.version}
    config = {k:v for k,v in vars(args).items() if k not in {'resume','retry_failed','source_dir','output_dir'}}
    implementation_hashes = {str(path.relative_to(REPO)):sha256(path)
        for path in sorted((REPO/'rnavail').rglob('*.py'))}
    if 'eternafold' in tools:
        from rnavail.adapters.eternafold import PARAMS_PATH
        if PARAMS_PATH.exists():
            implementation_hashes[str(PARAMS_PATH.relative_to(REPO))] = sha256(PARAMS_PATH)
    config.update(tools=tools,script_version=SCRIPT_VERSION,script_sha256=sha256(Path(__file__)),
        implementation_hashes=implementation_hashes,sources=source_manifest,tool_inventory=inventory)
    fingerprint = hashlib.sha256(json.dumps(config,sort_keys=True).encode()).hexdigest()
    output = args.output_dir
    if output.exists():
        if not args.resume:
            p.error('Output directory already exists; choose a new directory or --resume')
        old = json.loads((output/'manifest.json').read_text())
        if old['fingerprint']!=fingerprint:
            p.error('Resume configuration, sources, code or tool versions differ; choose a new output directory')
    else:
        output.mkdir(parents=True)
        dump_json(output/'manifest.json',{'fingerprint':fingerprint,'created_utc':datetime.now(timezone.utc).isoformat(),'config':config,
            'dataset':'GSE22393','source_url':'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE22393'})
    (output/'genes').mkdir(exist_ok=True)
    print('Loading and validating deposited inputs...',flush=True)
    sequences, genome = read_fasta(sources['transcripts']), read_fasta(sources['genome'])
    mapping = read_annotation(sources['annotation'])
    wig = read_wig(sources['pars'])
    intervals = defaultdict(list)
    for chrom,start,end in mapping.values():
        intervals[(chrom,start>end)].append((min(start,end),max(start,end)))
    names = sorted(set(args.gene) if args.gene else sequences)
    unknown = set(names)-sequences.keys()
    if unknown:
        p.error('Unknown transcript IDs: '+','.join(sorted(unknown)))
    models, statuses, rows = defaultdict(list), Counter(), []
    for number,name in enumerate(names,1):
        folder = output/'genes'/hashlib.sha256(name.encode()).hexdigest()[:24]
        folder.mkdir(exist_ok=True)
        checkpoint = folder/'result.json'
        result = json.loads(checkpoint.read_text()) if args.resume and checkpoint.exists() else None
        if result and args.retry_failed and (result['status']=='failed' or any(m['status']=='failed' for m in result.get('models',{}).values())):
            result = None
        if result is None:
            started = time.monotonic()
            result = {'transcript_id':name,'length':len(sequences[name]),'status':'ok','models':{},'windows':{},'fingerprint':fingerprint}
            try:
                sequence = Sequence(name,sequences[name])
                result['sequence_sha256'] = sequence.sha256
                if name not in mapping:
                    result.update(status='missing_annotation')
                elif sequence.has_ambiguous:
                    result.update(status='ambiguous_sequence')
                elif args.max_length and len(sequence)>args.max_length:
                    result.update(status='length_limit')
                else:
                    validate_mapping(sequence.seq,mapping[name],genome)
                    chrom,start,end = mapping[name]
                    pars, ambiguous = map_measurements(mapping[name],wig,intervals[(chrom,not(start>end))],not args.keep_antisense_overlaps)
                    result.update(n_measured=len(pars),coverage=len(pars)/len(sequence),n_antisense_measured=ambiguous,
                        chromosome=chrom,genome_start=start,genome_end=end,
                        mean_pars=statistics.mean(pars.values()) if pars else None)
                    if len(pars)<args.min_pairs:
                        result['status'] = 'insufficient_measurements'
                    else:
                        local_window = len(sequence) if args.local_scope=='full' else min(args.window_size,len(sequence))
                        local_span = local_window if args.local_scope=='full' else min(args.max_bp_span,local_window)
                        settings = ModelSettings(temperature_c=args.temperature,window_size=local_window,max_bp_span=local_span)
                        positions = sorted(pars)
                        # Only measured positions are necessary for marginal model comparison.
                        regions = [Region(pos,pos) for pos in positions]
                        predictions = {}
                        for tool in tools:
                            print(f'[{number}/{len(names)}] {name} ({len(sequence)} nt): {tool}',flush=True)
                            try:
                                if not inventory[tool]['available']:
                                    result['models'][tool] = {'status':'unavailable','error':'Required prediction tool is not installed'}
                                    continue
                                if tool=='rnaplfold':
                                    table = V.local_unpaired_matrix(sequence.seq,settings,min(args.footprint,local_window))
                                    predicted = {pos:V.region_probability_from_table(table,Region(pos,pos)) for pos in positions}
                                    predicted = {pos:1-p for pos,p in predicted.items() if p is not None}
                                    windows = list(window_records(sequence,pars,table,args.footprint,args.seed_length,args.step,args.min_window_coverage))
                                    for metric in ['full_p','seed_p']:
                                        result['windows'][metric] = correlation_stats([w['mean_pars'] for w in windows],[w[metric] for w in windows],args.min_pairs)
                                    seed_windows = [w for w in windows if w['seed_mean_pars'] is not None and w['seed_n_measured']/args.seed_length>=args.min_window_coverage]
                                    result['windows']['seed_p_vs_seed_pars'] = correlation_stats([w['seed_mean_pars'] for w in seed_windows],[w['seed_p'] for w in seed_windows],args.min_pairs)
                                    result['window_protocol'] = {'scope':'local','window_size':local_window,'max_bp_span':local_span,'footprint':args.footprint,'seed_length':args.seed_length,'step':args.step,'seed_mode':'best single segment among all contiguous placements'}
                                    if args.details:
                                        write_tsv_gz(folder/'windows.tsv.gz',windows,WINDOW_COLUMNS)
                                    protocol = {'scope':'local','settings':settings.to_dict(),
                                        'actual_max_unpaired':min(args.footprint,local_window),
                                        'version':inventory[tool]['version']}
                                else:
                                    request = AccessibilityRequest(sequence,regions,settings,recognition=RecognitionSpec(binder_class='structural_probe'))
                                    prediction = adapters[tool].run_accessibility(request)
                                    if not prediction.ok:
                                        result['models'][tool] = {'status':prediction.status,'error':prediction.error,'warnings':prediction.warnings}
                                        continue
                                    predicted = {pos:1-prediction.regions[f'{pos}-{pos}'].values['mean_base_unpaired'] for pos in positions}
                                    protocol = {'scope':'global','applied_protocol':prediction.applied_protocol,'version':prediction.version,'warnings':prediction.warnings}
                                matched = [pos for pos in positions if pos in predicted]
                                stats = correlation_stats([pars[pos] for pos in matched],[predicted[pos] for pos in matched],args.min_pairs)
                                result['models'][tool] = dict(stats,status='ok',protocol=protocol)
                                predictions[tool] = predicted
                            except Exception as exc:
                                result['models'][tool] = {'status':'failed','error':f'{type(exc).__name__}: {exc}'}
                        if args.details:
                            detail_rows = ({'transcript_position':pos,'base':sequence.seq[pos-1],
                                'genome_position':start+(pos-1)*(1 if start<=end else -1),'pars':pars[pos],
                                **{tool:predictions.get(tool,{}).get(pos) for tool in tools}} for pos in positions)
                            write_tsv_gz(folder/'per_base.tsv.gz',detail_rows,['transcript_position','base','genome_position','pars']+tools)
                        if not any(m['status']=='ok' for m in result['models'].values()):
                            result['status'] = 'no_successful_models'
                        elif any(m['status']!='ok' for m in result['models'].values()):
                            result['status'] = 'partial_model_failure'
            except Exception as exc:
                result.update(status='failed',error=f'{type(exc).__name__}: {exc}')
            result['runtime_s'] = time.monotonic()-started
            # Successful and skipped genes both have checkpoints and remain in the report.
            dump_json(checkpoint,result)
        if result['fingerprint']!=fingerprint:
            raise ValueError('Checkpoint fingerprint mismatch')
        statuses[result['status']] += 1
        base = {k:result.get(k) for k in ['transcript_id','length','status','n_measured','coverage','n_antisense_measured','mean_pars','error']}
        base['report'] = str((folder/'REPORT.md').relative_to(output))
        if not result.get('models'):
            rows.append(dict(base,model='',model_status=result['status']))
        for tool,m in result.get('models',{}).items():
            rows.append(dict(base,model=tool,model_status=m['status'],n_pairs=m.get('n_pairs'),pearson=m.get('pearson'),spearman=m.get('spearman'),model_error=m.get('error')))
            if m['status']=='ok' and m['n_pairs']:
                models['per_base:'+tool].append(m)
        for metric,m in result.get('windows',{}).items():
            if m['n_pairs']:
                models['window:'+metric].append(m)
        (folder/'REPORT.md').write_text(gene_report(result))
    aggregate = summarize_models(models,args.min_pairs)
    dump_json(output/'summary.json',{'fingerprint':fingerprint,'n_selected_transcripts':len(names),
        'n_deposited_transcripts':len(sequences),'n_annotation_only_transcripts':len(set(mapping)-sequences.keys()),
        'transcript_status_counts':dict(statuses),
        'model_status_counts':dict(Counter(r['model_status'] for r in rows if r['model'])),
        'statistics':aggregate})
    columns = ['transcript_id','length','status','model','model_status','n_measured','coverage','n_antisense_measured','mean_pars','n_pairs','pearson','spearman','error','model_error','report']
    with (output/'per_gene.tsv').open('w') as stream:
        writer = csv.DictWriter(stream,columns,delimiter='\t')
        writer.writeheader(); writer.writerows(rows)
    (output/'REPORT.md').write_text(aggregate_report(len(names),statuses,aggregate))
    print(f'Finished. Report: {output/"REPORT.md"}',flush=True)


def write_tsv_gz(path, rows, columns):
    with gzip.open(path,'wt') as stream:
        writer = csv.DictWriter(stream,columns,delimiter='\t')
        writer.writeheader(); writer.writerows(rows)


def display(value):
    return 'undefined' if value is None else f'{value:.4f}'


def gene_report(result):
    lines = [f'# {result["transcript_id"]}\n',f'Status: {result["status"]}. Length: {result["length"]} nt. Measured usable bases: {result.get("n_measured",0)}.\n']
    if result.get('error'):
        lines.append(result['error']+'\n')
    lines.append('| Model | Status | Matched bases | Pearson r | Spearman rho |\n| --- | --- | --- | --- | --- |\n')
    for name,m in result.get('models',{}).items():
        lines.append(f'| {name} | {m["status"]} | {m.get("n_pairs",0)} | {display(m.get("pearson"))} | {display(m.get("spearman"))} |\n')
    errors = [(name,m['error']) for name,m in result.get('models',{}).items() if m.get('error')]
    if errors:
        lines.append('\nModel errors:\n\n')
        lines.extend(f'- {name}: {error}\n' for name,error in errors)
    lines.append('\nPositive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.\n')
    lines.append('\n| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |\n| --- | --- | --- | --- |\n')
    for name,m in result.get('windows',{}).items():
        lines.append(f'| {name} | {m["n_pairs"]} | {display(m["pearson"])} | {display(m["spearman"])} |\n')
    lines.append('\nNegative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).\n')
    return ''.join(lines)


def aggregate_report(n, statuses, aggregate):
    lines = [f'# All-transcript Kertesz 2010 comparison\n\nSelected deposited transcripts: {n}. Status counts: {dict(statuses)}.\n\n',
        '| Comparison | Matched observations | Pooled Pearson | Median per-gene Pearson | Median per-gene Spearman |\n| --- | --- | --- | --- | --- |\n']
    for name,s in sorted(aggregate.items()):
        lines.append(f'| {name} | {s["n_pairs"]} | {display(s["pooled_pearson"])} | {display(s["median_gene_pearson"])} | {display(s["median_gene_spearman"])} |\n')
    lines.append('\nPer-base comparisons match experimental PARS with predicted pairing probability (expected positive association). Local-window diagnostics compare mean PARS with 20-nt joint opening and the best contiguous 8-nt seed (expected negative tendency); actual footprint/seed settings are recorded in the manifest. These diagnostics are not validation of joint opening, binding or strand displacement. No experimental values constrain the predictions.\n\n'
        'Pooled Pearson weights long, well-covered transcripts more heavily and combines within- and between-transcript effects. Median per-gene correlations give a complementary view with equal weight per defined gene correlation. Pooled Spearman and significance tests are deliberately absent: nearby bases, overlapping transcripts/windows and seed selection violate simple independence assumptions. No genome-wide accuracy claim follows from a handful of illustrative windows.\n\n'
        'Missing PARS entries remain missing; measured zero is preserved. Default handling excludes measured positions overlapping an oppositely oriented annotated transcript because the deposited WIG has no strand label. Input sequences must exactly reconstruct from the matching sacCer2 genome before use. Skipped genes and model failures remain visible; no length ceiling is applied unless explicitly requested. All deposited transcript records are considered, including noncoding records; this is not every genomic yeast gene. Experimental buffer and temperature are not asserted to match the computational conditions.\n\n'
        '[Per-gene table and individual report links](per_gene.tsv) · [Aggregate statistics](summary.json) · [Provenance and settings](manifest.json)\n')
    return ''.join(lines)


if __name__=='__main__':
    main()
