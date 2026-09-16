"""Expand the prior experimental sites to 20 nt and evaluate 8-nt seeds.

Run from the repository root with .venv/bin/python validation/controls_2010/run_seed_demo.py
"""
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from run_validation import (Sequence, Region, ModelSettings, RecognitionSpec,
    ConditionSpec, evaluate, TOOLS, to_json, to_tsv, to_text, to_html,
    build_candidate_visuals, table)


def main():
    baseline = json.loads((ROOT/'validation_summary.json').read_text())['experimental']
    summary = []
    for name, info in baseline.items():
        original = ROOT/name
        sequence = Sequence(info['gene'], ''.join((original/'target.fa').read_text().splitlines()[1:]))
        regions = []
        for label in ['low','high']:
            old_start = info[label][1]
            # Center on the old 8-nt site, keeping the complete 20-nt
            # footprint within the previously compared experimental domain.
            start = max(info['lo'], min(old_start-6, info['hi']-19))
            regions.append(Region(start,start+19,f'around_PARS_{label}_20nt'))
        folder = original/'seed_20nt'
        folder.mkdir(exist_ok=True)
        (folder/'target.fa').write_text(f'>{sequence.name}\n{sequence.seq}\n')
        settings = ModelSettings(temperature_c=37,window_size=len(sequence),max_bp_span=len(sequence))
        recognition = RecognitionSpec(binder_class='antisense_oligo',seed_lengths=(8,),seed_mode='any')
        report = evaluate(sequence,regions,settings=settings,recognition=recognition,
            condition=ConditionSpec(condition_id='validation_model_37C',temperature_c=37),
            tools=TOOLS,seed_length=8,options={'samples':10000,'sampling_seed':1729},
            progress=lambda s:print(name,s,flush=True))
        assert not report.tools_failed and not report.tools_skipped
        to_json(report,folder/'report.json')
        to_tsv(report,folder/'metrics.tsv')
        (folder/'report.txt').write_text(to_text(report,verbose=True))
        visuals={c.key:build_candidate_visuals(sequence,c.region,settings,flank=len(sequence)) for c in report.candidates}
        to_html(report,visuals,folder/'report.html')
        exact=next(t for t in report.tool_results if t.tool=='vienna-exact')
        rows=[]
        for region in regions:
            values=exact.regions[f'{region.start}-{region.end}'].values
            p,seed=values['p_unpaired'],values['seed_p_unpaired']
            start=int(values['seed_start'])
            assert seed+1e-8>=p
            assert region.start<=start<=region.end-7
            row=[name,f'{region.start}–{region.end}',f'{p:.6g}',f'{seed:.6g}',f'{start}–{start+7}',f'{values["dg_open"]:.3f}',f'{values["seed_dg_open"]:.3f}']
            rows.append(row[1:]); summary.append(row)
        columns=['20-nt target','Full-site P','Best 8-nt seed P','Seed coordinates','Full-site opening cost','Seed opening cost']
        description=(f'# {name}: 20-nt targets with 8-nt seeds\n\n'
            'Both target intervals extend the previously selected PARS-low and PARS-high 8-nt sites by six bases on each side, clamped to the original experimental comparison domain. They were not selected by scanning predicted accessibility. “Around PARS-low/high” describes the original anchor, not an experimental classification of the expanded 20-nt region.\n\n'
            'The complete deposited transcript is folded at 37 °C with Turner 2004 and dangles=2; local window/span equal transcript length and global pairing is unrestricted. Recognition is declared as antisense_oligo. No partner sequence or interaction energy is calculated, and experimental measurements do not constrain the predictions.\n\n'
            'The table uses global ViennaRNA constrained partition functions for both probabilities and energies (kcal/mol). Seed mode is any: all 13 possible contiguous 8-nt placements within each 20-nt target are examined, and the one with highest opening probability is reported. Best-seed P is the probability of that particular chosen segment being open; it is not the probability that at least one of the 13 segments is open.\n\n'
            +table(rows,columns)+'\n'
            +'\n'+table([[r.label,r.slice(sequence)] for r in regions],['Target label','20-nt sequence'])
            +'\nA short seed can be exposed while much of the remaining footprint is paired. Seed P describes a possible initiation opportunity; it does not predict oligo binding, strand invasion or displacement success. PARS is a per-base assay and cannot directly validate either joint probability.\n\n'
            +('The expanded RPL41A windows overlap by two bases; they are illustrative regions, not independent replicates.\n\n' if regions[0].overlaps(regions[1]) else '')
            +'Eight adapters completed successfully; sampling uses 10,000 structures and seed 1729. Per-adapter observations and estimator scopes remain in the JSON.\n\n'
            +'[Visual report](report.html) · [JSON](report.json) · [Metrics](metrics.tsv) · [Input](target.fa)\n')
        (folder/'REPORT.md').write_text(description)
        print(table(rows,columns),flush=True)
    (ROOT/'SEED_DEMO.md').write_text('# 20-nt target / 8-nt seed demonstration\n\n'
        +table(summary,['Transcript','20-nt target','Full-site P','Best 8-nt seed P','Seed coordinates','Full-site opening kcal/mol','Seed opening kcal/mol'])
        +'\nThese are unconditioned full-transcript predictions for oligo-style recognition. Best-seed P refers to one selected 8-nt segment, rather than the union of all possible seeds. PARS measurements do not directly validate joint opening or oligo binding.\n\n'
        +'[CCW12 report](CCW12/seed_20nt/REPORT.md) · [RPL41A report](RPL41A/seed_20nt/REPORT.md)\n\n'
        +'Reproduce from the repository root:\n\n```bash\n.venv/bin/python validation/controls_2010/run_seed_demo.py\n```\n')


if __name__=='__main__':
    main()
