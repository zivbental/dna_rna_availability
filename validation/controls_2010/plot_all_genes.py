"""Make standalone figures and an interpretation from a completed comparison."""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
import statistics


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('run_dir',type=Path,nargs='?',default=Path(__file__).parent/'all_genes_comparison')
    args = parser.parse_args()
    root = args.run_dir
    # summary.json is written only after all selected transcripts have been collected.
    summary = json.loads((root/'summary.json').read_text())
    manifest = json.loads((root/'manifest.json').read_text())
    assert summary['fingerprint']==manifest['fingerprint']
    with (root/'per_gene.tsv').open() as stream:
        rows = list(csv.DictReader(stream,delimiter='\t'))
    n_genes = len({r['transcript_id'] for r in rows})
    assert n_genes==summary['n_selected_transcripts']
    models = sorted({r['model'] for r in rows if r['model_status']=='ok'})
    by_gene = {model:{r['transcript_id']:float(r['pearson']) for r in rows
        if r['model']==model and r['model_status']=='ok' and r['pearson']!=''} for model in models}
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    import numpy as np
    bins = np.linspace(-1,1,41)
    figure,axes = plt.subplots(1,len(models),figsize=(6*len(models),4),squeeze=False)
    for axis,model in zip(axes[0],models):
        values = list(by_gene[model].values())
        axis.hist(values,bins=bins,color='#4675a5',edgecolor='white',linewidth=.4)
        axis.axvline(0,color='black',linewidth=.8)
        if values:
            median = statistics.median(values)
            axis.axvline(median,color='#a84444',linestyle='--',label=f'Median r = {median:.3f}')
            axis.legend()
        axis.set(xlim=(-1,1),xlabel='Per-transcript Pearson r (PARS, predicted pairing)',ylabel='Transcripts',title=f'{model}: {len(values):,} defined correlations')
    figure.suptitle('Agreement with experimental per-base structure tendencies')
    figure.tight_layout()
    for extension in ['png','pdf']:
        figure.savefig(root/f'per_gene_correlations.{extension}',dpi=180)
    plt.close(figure)

    if {'rnaplfold','rnafold'}<=by_gene.keys():
        genes = sorted(by_gene['rnaplfold'].keys() & by_gene['rnafold'].keys())
        figure,axis = plt.subplots(figsize=(6,5))
        axis.hexbin([by_gene['rnaplfold'][g] for g in genes],
            [by_gene['rnafold'][g] for g in genes],gridsize=40,mincnt=1,cmap='Blues',extent=(-1,1,-1,1))
        axis.plot([-1,1],[-1,1],color='gray',linestyle='--',linewidth=1)
        axis.axhline(0,color='gray',linewidth=.5);axis.axvline(0,color='gray',linewidth=.5)
        axis.set(xlim=(-1,1),ylim=(-1,1),xlabel='RNAplfold per-gene r with PARS',ylabel='RNAfold per-gene r with PARS',title=f'Local versus global experimental agreement ({len(genes):,} transcripts)')
        figure.tight_layout()
        for extension in ['png','pdf']:
            figure.savefig(root/f'local_vs_global.{extension}',dpi=180)
        plt.close(figure)

    comparison = summary['statistics']
    lines = ['# Interpretation of the completed PARS comparison\n',
        f'All {n_genes:,} deposited transcript records were considered. Status counts: {summary["transcript_status_counts"]}. Mapping modes: {summary.get("mapping_mode_counts",{})}.\n',
        '| Per-base model | Matched bases | Pooled Pearson r | Median per-transcript r | Median per-transcript rho | Transcripts with positive r |\n| --- | --- | --- | --- | --- | --- |\n']
    for model in models:
        stat = comparison['per_base:'+model]
        fmt = lambda v:'undefined' if v is None else f'{v:.4f}'
        fraction = stat['fraction_genes_positive_pearson']
        positive = 'undefined' if fraction is None else f'{fraction:.1%}'
        lines.append(f'| {model} | {stat["n_pairs"]:,} | {fmt(stat["pooled_pearson"])} | {fmt(stat["median_gene_pearson"])} | {fmt(stat["median_gene_spearman"])} | {positive} |\n')
    lines.append('\nPositive PARS/pairing correlation means agreement in per-base structural tendency. Pooled r weights transcripts by measured bases and mixes within- and between-transcript effects. Per-transcript medians show the typical within-transcript association. These metrics concern secondary structure, not measured oligo binding or simultaneous footprint opening.\n\n![Per-transcript correlations](per_gene_correlations.png)\n')
    if {'rnaplfold','rnafold'}<=by_gene.keys():
        lines.append('\n![Local versus global agreement](local_vs_global.png)\n')
    lines.append('\n| Exploratory local-window metric | Covered windows | Pooled Pearson r | Median per-transcript r |\n| --- | --- | --- | --- |\n')
    for key,stat in comparison.items():
        if key.startswith('window:'):
            lines.append(f'| {key.split(":",1)[1]} | {stat["n_pairs"]:,} | {fmt(stat["pooled_pearson"])} | {fmt(stat["median_gene_pearson"])} |\n')
    lines.append('\nWindow metrics correlate mean PARS with full-site or best-seed opening probability; negative association is the expected tendency. The seed_p_vs_seed_pars diagnostic uses the selected seed’s own mean PARS. Overlapping windows, model-selected seed placements and correlated neighboring bases are not independent experiments. No p-values or calibrated classification accuracy are claimed.\n\n'
        'All predictions are independent of the PARS measurements. The local model uses the manifest’s window/span settings; the global model has unrestricted pairing. Default strand-ambiguous overlaps are excluded, missing measurements are preserved, and mature/processed transcripts must exactly reconstruct from the supplied exon/UTR blocks. Experimental solution conditions, proteins and tertiary contacts remain outside the models.\n\n'
        '[Full aggregate report](REPORT.md) · [Per-gene results and report paths](per_gene.tsv) · [Statistics](summary.json) · [Settings and provenance](manifest.json). Figure PDFs are available alongside the PNG files.\n')
    (root/'INTERPRETATION.md').write_text(''.join(lines))
    print(root/'INTERPRETATION.md')


if __name__=='__main__':
    main()
