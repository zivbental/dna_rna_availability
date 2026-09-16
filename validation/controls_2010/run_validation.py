"""Reproduce the control runs and independent Kertesz 2010 comparison.

Run from the repository root: .venv/bin/python validation/controls_2010/run_validation.py
Only the Python standard library and the repository's installed dependencies are used.
"""
from __future__ import annotations

import csv
import gzip
import hashlib
import json
import math
from pathlib import Path
import statistics
import sys
import time
import urllib.request

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT.parents[1]))
from rnavail.core.sequence import Sequence, Region
from rnavail.core.model import ModelSettings, RecognitionSpec, ConditionSpec
from rnavail.pipeline.run import evaluate
from rnavail.io.report import to_json, to_text, to_tsv
from rnavail.io.html_report import to_html
from rnavail.viz.generate import build_candidate_visuals
from rnavail.adapters import _vienna as V

TOOLS = ['rnaplfold', 'rnaplfold-cli', 'vienna-exact', 'rnafold',
         'ensemble-sample', 'rnastructure-partition', 'contrafold', 'eternafold']
BASE = 'https://ftp.ncbi.nlm.nih.gov/geo/series/GSE22nnn/GSE22393/suppl/'
FILES = ['GSE22393_sce_genes.fasta.gz', 'GSE22393_sce_0608.fasta.gz',
         'GSE22393_sce_transcriptome_global.tab.gz',
         'GSE22393_processed_merged_PARS_sacCer2_1.wig.gz']
PAPER = 'https://www.wisdom.weizmann.ac.il/~eran/kertesz_nature_2010.pdf'
GEO = 'https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE22393'


def fasta(path):
    records = {}
    with gzip.open(path, 'rt') as stream:
        for line in stream:
            if line.startswith('>'):
                name = line[1:].strip().split()[0]
                records[name] = ''
            else:
                records[name] += line.strip()
    return records


def pearson(x, y):
    if len(x) < 3:
        return None
    a, b = statistics.mean(x), statistics.mean(y)
    den = math.sqrt(sum((v-a)**2 for v in x)*sum((v-b)**2 for v in y))
    return sum((u-a)*(v-b) for u, v in zip(x, y))/den if den else None


def ranks(values):
    result = [0.] * len(values)
    ordered = sorted(range(len(values)), key=values.__getitem__)
    i = 0
    while i < len(values):
        j = i + 1
        while j < len(values) and values[ordered[j]] == values[ordered[i]]:
            j += 1
        for k in ordered[i:j]:
            result[k] = (i+j-1)/2
        i = j
    return result


def table(rows, columns):
    return '| ' + ' | '.join(columns) + ' |\n| ' + ' | '.join(['---']*len(columns)) + ' |\n' + ''.join('| ' + ' | '.join(str(v) for v in r) + ' |\n' for r in rows)


def main():
    source = ROOT / 'source'
    source.mkdir(exist_ok=True)
    for filename in FILES:
        path = source / filename
        if not path.exists():
            print('Downloading', filename, flush=True)
            with urllib.request.urlopen(BASE+filename, timeout=60) as response:
                path.write_bytes(response.read())
        with gzip.open(path, 'rb') as stream:
            stream.read(1)  # Refuse HTML/error pages masquerading as data.
    manifest = {f: {'url': BASE+f, 'sha256': hashlib.sha256((source/f).read_bytes()).hexdigest()} for f in FILES}
    (source/'manifest.json').write_text(json.dumps(manifest, indent=2)+'\n')
    sequences = fasta(source/FILES[0])
    genome = fasta(source/FILES[1])
    mapping = {}
    for line in gzip.open(source/FILES[2], 'rt'):
        name, chromosome, start, end, feature = line.strip().split('\t')
        if feature == 'Transcript':
            mapping[name] = (chromosome, int(start), int(end))

    # Figure 2 explicitly labels these as transcript base coordinates.
    papers = [('CCW12', 'YLR110C', 50, 110, '2a,b'),
              ('RPL41A', 'YDL184C', 50, 120, '2c,d')]
    wanted = {}
    for name, gene, lo, hi, figure in papers:
        chrom, start, end = mapping[gene]
        reverse = start > end
        segment = genome[chrom][min(start,end)-1:max(start,end)]
        if reverse:
            segment = segment.translate(str.maketrans('ACGT','TGCA'))[::-1]
        assert segment == sequences[gene], f'Genome/transcript mismatch: {gene}'
        roman = ['I','II','III','IV','V','VI','VII','VIII','IX','X','XI','XII','XIII','XIV','XV','XVI'][int(chrom)-1]
        wanted[name] = ('chr'+roman, start, -1 if reverse else 1, lo, hi)
    pars = {name: {} for name, *_ in papers}
    chromosome = None
    for line in gzip.open(source/FILES[3], 'rt'):
        if line.startswith('variableStep'):
            chromosome = line.split('chrom=')[1].split()[0]
        elif line[0].isdigit():
            coordinate, value = line.split()
            for name, (chrom, start, direction, lo, hi) in wanted.items():
                pos = (int(coordinate)-start)*direction+1
                if chromosome == chrom and 1 <= pos <= len(sequences[dict((n,g) for n,g,*_ in papers)[name]]):
                    pars[name][pos] = float(value)

    stem = 'GCGCGCGCGCGCGCGCGCGC'
    cases = [
        ('open_AC', Sequence('open_AC', 'AC'*24), [Region(5,12,'open_8nt'),Region(5,24,'open_20nt')],
         'Designed positive control: A/C-only RNA has no AU, GC or GU pairing partners under the canonical secondary-structure model. Expected joint opening probability: 1.'),
        ('closed_hairpin', Sequence('closed_hairpin', stem+'A'*8+stem),
         [Region(5,12,'stem_8nt'),Region(1,20,'stem_20nt'),Region(21,28,'loop_8nt')],
         'Designed negative control: a 20-bp GC stem encloses an 8-A loop. The central stem should be strongly buried; the loop provides an open site in the same molecule. This is a model control, not an experimentally measured construct.'),
        ('disrupted_hairpin', Sequence('disrupted_hairpin', stem+'A'*8+'A'*20),
         [Region(5,12,'same_site_8nt'),Region(1,20,'same_site_20nt')],
         'Stem-disruption control: replace the opposing GC arm with 20 A bases, preserving length and the tested arm. Residual folding within the GC arm is possible, so complete opening is not guaranteed; the expectation is increased accessibility relative to the intact hairpin.'),
    ]
    experimental = {}
    for name, gene, lo, hi, figure in papers:
        # Select by experimental signal only, before any predictions are run.
        windows = []
        for start in range(lo, hi-8+2):
            observed = [pars[name][p] for p in range(start,start+8) if p in pars[name]]
            if len(observed) >= 6:
                windows.append((statistics.mean(observed), start, len(observed)))
        assert windows, f'Insufficient experimental coverage: {name}'
        low = min(windows)
        # Ensure that the two illustrative sites do not overlap.
        high = max(w for w in windows if abs(w[1]-low[1]) >= 8)
        regions = [Region(low[1],low[1]+7,'PARS_low_8nt'),Region(high[1],high[1]+7,'PARS_high_8nt')]
        seq = Sequence(gene, sequences[gene])
        cases.append((name, seq, regions,
            f'Experimentally footprinted example from Figure {figure}: {gene}, transcript bases {lo}–{hi}. Prediction uses the complete deposited {len(seq)}-nt transcript. Sites are the lowest mean PARS 8-nt window and the highest non-overlapping mean PARS window with at least 6/8 measured bases; neither is selected using predictions.'))
        experimental[name] = {'gene':gene,'lo':lo,'hi':hi,'figure':figure,'low':low,'high':high}

    summary = []
    all_checks = []
    for name, seq, regions, description in cases:
        folder = ROOT/name
        folder.mkdir(exist_ok=True)
        (folder/'target.fa').write_text(f'>{seq.name}\n{seq.seq}\n')
        settings = ModelSettings(temperature_c=37, window_size=len(seq), max_bp_span=len(seq))
        condition = ConditionSpec(condition_id='validation_model_37C', temperature_c=37)
        started = time.monotonic()
        print('Running',name,flush=True)
        report = evaluate(seq, regions, settings=settings, condition=condition,
            recognition=RecognitionSpec(binder_class='structural_probe', seed_lengths=(8,)), tools=TOOLS,
            seed_length=8, options={'samples':10000,'sampling_seed':1729},
            progress=lambda s: print(' ',s,flush=True))
        to_json(report, folder/'report.json')
        to_tsv(report, folder/'metrics.tsv')
        (folder/'report.txt').write_text(to_text(report,verbose=True))
        visuals = {c.key:build_candidate_visuals(seq,c.region,settings,flank=len(seq)) for c in report.candidates}
        to_html(report,visuals,folder/'report.html')
        exact = next(t for t in report.tool_results if t.tool=='vienna-exact')
        assert exact.ok, exact.error
        lines = [f'# {name}\n',description+'\n',
            'RNA, Turner 2004, 37 °C, dangles=2, unrestricted global pairing. Local window and pair span equal the full transcript length for a matched-scope comparison. Experimental buffer/temperature are not asserted to match this computational protocol. Magnesium, tertiary contacts, proteins and cellular binding are not modeled. No experimental data constrain any prediction. All coordinates are one-based and inclusive.\n']
        rows = []
        for r in regions:
            m = exact.regions[f'{r.start}-{r.end}'].values
            p,dg = m['p_unpaired'],m['dg_open']
            rows.append([r.label,f'{r.start}–{r.end}',r.slice(seq),f'{p:.6g}',f'{dg:.4f}'])
            summary.append([name,r.label,f'{p:.6g}',f'{dg:.4f}'])
        lines.append(table(rows,['Site','Coordinates','Sequence','Joint P(open), global exact','Opening cost (kcal/mol)']))
        cross_model = []
        for tool in report.tool_results:
            for region in regions:
                values = tool.regions.get(f'{region.start}-{region.end}')
                if values is not None:
                    values = values.values
                    cross_model.append([tool.tool, region.label,
                        f'{values["p_unpaired"]:.6g}' if 'p_unpaired' in values else 'not provided',
                        f'{values["mean_base_unpaired"]:.6g}' if 'mean_base_unpaired' in values else 'not provided'])
        lines.append('\n'+table(cross_model,['Adapter','Site','Joint P(open)','Mean per-base P(unpaired), distinct diagnostic']))
        lines.append('\nThe heuristic rank is not used as a pass/fail criterion. Compare probabilities and opening costs under the same scope and footprint.\n')
        if name in experimental:
            info = experimental[name]
            # Batch all positions into one calculation per model, for a
            # measurement-matched comparison beyond the ViennaRNA family.
            diagnostic = evaluate(seq,
                [Region(p,p,f'nt_{p}') for p in range(info['lo'],info['hi']+1)],
                settings=settings, tools=['rnafold','rnastructure-partition','contrafold','eternafold'])
            to_json(diagnostic,folder/'per_base_models.json')
            assert not diagnostic.tools_failed and not diagnostic.tools_skipped, 'Per-base model adapter failure'
            fc = V.make_fold_compound(seq.seq, settings)
            energy = fc.mfe()[1]
            fc.exp_params_rescale(energy)
            fc.pf()
            unpaired = V.unpaired_probabilities(fc)
            positions = [p for p in range(info['lo'],info['hi']+1) if p in pars[name]]
            x = [pars[name][p] for p in positions]
            y = [1-unpaired[p] for p in positions]
            rp,rs = pearson(x,y),pearson(ranks(x),ranks(y))
            with (folder/'experimental_comparison.tsv').open('w') as stream:
                writer = csv.writer(stream,delimiter='\t')
                model_names = [t.tool for t in diagnostic.tool_results]
                writer.writerow(['transcript_position','base','genome_chromosome','genome_position','PARS_score'] + [n+'_pairing_probability' for n in model_names])
                chrom,start,direction,_,_ = wanted[name]
                for p in range(info['lo'],info['hi']+1):
                    probabilities = [1-t.regions[f'{p}-{p}'].values['mean_base_unpaired'] for t in diagnostic.tool_results]
                    writer.writerow([p,seq.seq[p-1],chrom,start+direction*(p-1),pars[name].get(p,'')] + probabilities)
            model_correlations = []
            for tool in diagnostic.tool_results:
                probabilities = [1-tool.regions[f'{p}-{p}'].values['mean_base_unpaired'] for p in positions]
                model_correlations.append([tool.tool,pearson(x,probabilities),pearson(ranks(x),ranks(probabilities))])
            lines.append('\n'+table([[n,f'{r:.4f}',f'{s:.4f}'] for n,r,s in model_correlations],['Per-base prediction model','Pearson r with PARS','Spearman rho with PARS']))
            comparison = []
            for label,window in [('PARS_low_8nt',info['low']),('PARS_high_8nt',info['high'])]:
                mean,start,n = window
                comparison.append([label,f'{mean:.3f}',f'{n}/8',f'{statistics.mean(1-unpaired[p] for p in range(start,start+8)):.4f}'])
            lines.extend(['\n'+table(comparison,['Site','Mean measured PARS','Measured bases','Mean predicted pairing']),
                f'\nWithin the footprinted domain: {len(positions)}/{info["hi"]-info["lo"]+1} bases have deposited PARS values. Pearson r(PARS, predicted pairing) = {rp:.4f}; Spearman rho = {rs:.4f}. Positive correlation is the expected direction. These are descriptive statistics from one small domain, without a significance or genome-wide accuracy claim.\n',
                'Missing WIG entries stay missing; a measured zero stays zero. The WIG already contains processed PARS scores at nucleotide coordinates, so no additional downstream cleavage shift is applied. Its lack of strand labels can make antisense overlaps ambiguous. Genome reconstruction is checked against the deposited transcript FASTA before comparison.\n',
                'Higher PARS means greater double-stranded tendency; lower PARS means greater single-stranded tendency. These assays do not measure joint opening of an 8-nt footprint or successful binding. The selected windows are relative extrema, not guaranteed binary open/closed labels. Raw cleavage depth and per-base uncertainty are not available in this processed track. Traditional gel validation concerns the domain, not a separate assay of each selected window.\n',
                f'[Paper, Figure {info["figure"]}]({PAPER}); [deposited experimental data]({GEO}).\n'])
            low = exact.regions[f'{info["low"][1]}-{info["low"][1]+7}'].values['p_unpaired']
            high = exact.regions[f'{info["high"][1]}-{info["high"][1]+7}'].values['p_unpaired']
            verdict = 'direction agrees' if low > high else 'direction disagrees'
            lines.append(f'\nIllustrative window comparison: **{verdict}** with the experimental ordering (PARS-low joint P={low:.6g}; PARS-high joint P={high:.6g}). This ordering is supplementary because PARS and joint opening are different measurements.\n')
            info.update(pearson=rp,spearman=rs,n_measured=len(positions),window_order=verdict,
                model_correlations={n:{'pearson':r,'spearman':s} for n,r,s in model_correlations})
            import matplotlib
            matplotlib.use('Agg')
            import matplotlib.pyplot as plt
            fig,ax=plt.subplots(2,1,figsize=(10,6),sharex=True)
            ax[0].bar(positions,x,color=['#b54b4b' if v>0 else '#348b62' for v in x])
            ax[0].axhline(0,color='black',lw=.6); ax[0].set_ylabel('Measured PARS')
            ax[1].plot(range(info['lo'],info['hi']+1),[1-unpaired[p] for p in range(info['lo'],info['hi']+1)])
            ax[1].set_ylabel('Predicted P(paired)'); ax[1].set_ylim(0,1); ax[1].set_xlabel('Transcript nucleotide (1-based)')
            fig.suptitle(f'{name}: experimental signal and unconditioned full-transcript prediction')
            fig.tight_layout(); fig.savefig(folder/'experimental_comparison.png',dpi=180); plt.close(fig)
            lines.append('\n![Experimental comparison](experimental_comparison.png)\n')
        else:
            if name == 'disrupted_hairpin':
                lines.append('\nThe disrupted construct remains mostly closed: removing an opposing arm does not make this repetitive GC sequence unstructured. Its GC arm can form a shorter hairpin within itself. This is a directional perturbation control, not a positive open control; use open_AC or the A-only loop for the positive control.\n')
            sweeps = []
            for temp in [25,37,50]:
                small = evaluate(seq,regions,settings=ModelSettings(temperature_c=temp,window_size=len(seq),max_bp_span=len(seq)),tools=['vienna-exact'],seed_length=8)
                tool=small.tool_results[0]
                for r in regions:
                    m=tool.regions[f'{r.start}-{r.end}'].values
                    sweeps.append([temp,r.label,m['p_unpaired'],m['dg_open']])
            (folder/'temperature_sweep.json').write_text(json.dumps(sweeps,indent=2)+'\n')
            lines.append('\n'+table([[t,l,f'{p:.6g}',f'{d:.4f}'] for t,l,p,d in sweeps],['Temperature °C','Site','Joint P(open)','Opening cost']))
        statuses = [[t.tool,t.status,t.version,t.error or '—'] for t in report.tool_results]
        lines.append('\n'+table(statuses,['Adapter','Status','Version','Error']))
        lines.append(f'\nElapsed run time: {time.monotonic()-started:.2f} s. [Visual pipeline report](report.html), [full JSON](report.json), [metrics TSV](metrics.tsv), [input FASTA](target.fa). Heatmaps use the complete transcript, matching the prediction scope.\n')
        (folder/'REPORT.md').write_text('\n'.join(lines))
        all_checks.append({'case':name,'tools_failed':report.tools_failed,'tools_skipped':report.tools_skipped})

    def val(name,key):
        d=json.loads((ROOT/name/'report.json').read_text())
        t=next(t for t in d['tool_results'] if t['tool']=='vienna-exact')
        return t['regions'][key]['values']['p_unpaired']
    checks={'open_control_P_equals_one':abs(val('open_AC','5-12')-1)<1e-9,
        'closed_stem_P_below_1e_minus_6':val('closed_hairpin','5-12')<1e-6,
        'hairpin_loop_P_above_0_99':val('closed_hairpin','21-28')>.99,
        'stem_disruption_increases_accessibility':val('disrupted_hairpin','5-12')>val('closed_hairpin','5-12'),
        'no_adapter_failures':all(not c['tools_failed'] and not c['tools_skipped'] for c in all_checks)}
    (ROOT/'validation_summary.json').write_text(json.dumps({'checks':checks,'experimental':experimental,'runs':all_checks},indent=2)+'\n')
    overview=['# Accessibility controls and Kertesz 2010 validation\n',
        'Five actual pipeline runs: three designed model controls and two experimentally footprinted paper examples. All predictions are independent of the PARS measurements. These results concern isolated RNA secondary structure; no sequence is guaranteed permanently open or closed across all physical conditions.\n',
        table(summary,['Case','Site','Joint P(open), global exact','Opening cost kcal/mol']),
        '\n'+table([[k,'PASS' if v else 'FAIL'] for k,v in checks.items()],['Predeclared model sanity check','Result']),
        '\n'+table([[n,f'{d["pearson"]:.4f}',f'{d["spearman"]:.4f}',d['window_order']] for n,d in experimental.items()],['Footprinted example','Pearson r(PARS,pairing)','Spearman rho','Selected window ordering']),
        '\nRPL41A shows moderate per-base agreement across all four models (Pearson r about 0.57–0.62). CCW12 shows weak agreement for the thermodynamic models and slightly negative agreement for the learned models. Its selected windows have the expected mean per-base pairing ordering, but the opposite joint-opening ordering. This supports a limited benchmark, not a claim that the pipeline is experimentally validated for whole-site opening or binding. The synthetic stem-disruption construct also remains mostly closed; only open_AC and the A-only hairpin loop serve as positive open controls.\n',
        '\n'+''.join(f'- [{name}: individual report]({name}/REPORT.md) · [pipeline HTML]({name}/report.html)\n' for name,*_ in cases),
        '\nThe paper’s Figure 2 reports traditional RNase footprinting agreement for CCW12 and RPL41A. We compare the deposited PARS track with our predictions, rather than digitizing the gel. ASH1 and URE2 are discussed in the paper, but their matching transcript records are absent from the deposited filtered FASTA/annotation used here; no substitute sequence is presented as an exact reproduction.\n',
        f'[Kertesz et al., Nature 467, 103–107 (2010)]({PAPER}); [GSE22393 data]({GEO}).\n',
        '\nReproduce from the repository root:\n\n```bash\n.venv/bin/python validation/controls_2010/run_validation.py\n```\n',
        'The script verifies gzip inputs, archives download URLs and SHA256 hashes, confirms negative-strand coordinate conversion by reconstructing each complete transcript from the matching genome, preserves missing PARS values, selects windows from experiment alone, and writes every tool’s status/version. Sampling uses 10,000 draws and seed 1729. Eight adapters cover local/whole-transcript thermodynamics, sampling, an independent thermodynamic implementation, and two learned models; kinetic, pseudoknot, G4 and MFE-only extensions are outside this focused equilibrium comparison. RNAplfold CLI 2.4.7 and bindings 2.7.2 are a version-different parity check, not independent evidence. Experiments are annotations in the companion comparison, not SHAPE pseudoenergies.\n']
    (ROOT/'REPORT.md').write_text('\n'.join(overview))
    print(json.dumps(checks,indent=2),flush=True)
    if not all(checks.values()):
        raise SystemExit('One or more model controls or adapter checks failed; see reports.')


if __name__ == '__main__':
    main()
