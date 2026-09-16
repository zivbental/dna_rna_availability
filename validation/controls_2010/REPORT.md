# Accessibility controls and Kertesz 2010 validation

Five actual pipeline runs: three designed model controls and two experimentally footprinted paper examples. All predictions are independent of the PARS measurements. These results concern isolated RNA secondary structure; no sequence is guaranteed permanently open or closed across all physical conditions.

| Case | Site | Joint P(open), global exact | Opening cost kcal/mol |
| --- | --- | --- | --- |
| open_AC | open_8nt | 1 | 0.0000 |
| open_AC | open_20nt | 1 | 0.0000 |
| closed_hairpin | stem_8nt | 2.52178e-19 | 26.3939 |
| closed_hairpin | stem_20nt | 3.5841e-25 | 34.6921 |
| closed_hairpin | loop_8nt | 1 | 0.0000 |
| disrupted_hairpin | same_site_8nt | 1.04986e-08 | 11.3233 |
| disrupted_hairpin | same_site_20nt | 1.07337e-13 | 18.4054 |
| CCW12 | PARS_low_8nt | 0.00734829 | 3.0282 |
| CCW12 | PARS_high_8nt | 0.0136473 | 2.6467 |
| RPL41A | PARS_low_8nt | 0.0178501 | 2.4812 |
| RPL41A | PARS_high_8nt | 0.00041534 | 4.7990 |


| Predeclared model sanity check | Result |
| --- | --- |
| open_control_P_equals_one | PASS |
| closed_stem_P_below_1e_minus_6 | PASS |
| hairpin_loop_P_above_0_99 | PASS |
| stem_disruption_increases_accessibility | PASS |
| no_adapter_failures | PASS |


| Footprinted example | Pearson r(PARS,pairing) | Spearman rho | Selected window ordering |
| --- | --- | --- | --- |
| CCW12 | 0.2522 | 0.2186 | direction disagrees |
| RPL41A | 0.5870 | 0.6117 | direction agrees |

RPL41A shows moderate per-base agreement across all four models (Pearson r about 0.57–0.62). CCW12 shows weak agreement for the thermodynamic models and slightly negative agreement for the learned models. Its selected windows have the expected mean per-base pairing ordering, but the opposite joint-opening ordering. This supports a limited benchmark, not a claim that the pipeline is experimentally validated for whole-site opening or binding. The synthetic stem-disruption construct also remains mostly closed; only open_AC and the A-only hairpin loop serve as positive open controls.


- [open_AC: individual report](open_AC/REPORT.md) · [pipeline HTML](open_AC/report.html)
- [closed_hairpin: individual report](closed_hairpin/REPORT.md) · [pipeline HTML](closed_hairpin/report.html)
- [disrupted_hairpin: individual report](disrupted_hairpin/REPORT.md) · [pipeline HTML](disrupted_hairpin/report.html)
- [CCW12: individual report](CCW12/REPORT.md) · [pipeline HTML](CCW12/report.html)
- [RPL41A: individual report](RPL41A/REPORT.md) · [pipeline HTML](RPL41A/report.html)


The paper’s Figure 2 reports traditional RNase footprinting agreement for CCW12 and RPL41A. We compare the deposited PARS track with our predictions, rather than digitizing the gel. ASH1 and URE2 are discussed in the paper, but their matching transcript records are absent from the deposited filtered FASTA/annotation used here; no substitute sequence is presented as an exact reproduction.

[Kertesz et al., Nature 467, 103–107 (2010)](https://www.wisdom.weizmann.ac.il/~eran/kertesz_nature_2010.pdf); [GSE22393 data](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE22393).


Reproduce from the repository root:

```bash
.venv/bin/python validation/controls_2010/run_validation.py
```

The script verifies gzip inputs, archives download URLs and SHA256 hashes, confirms negative-strand coordinate conversion by reconstructing each complete transcript from the matching genome, preserves missing PARS values, selects windows from experiment alone, and writes every tool’s status/version. Sampling uses 10,000 draws and seed 1729. Eight adapters cover local/whole-transcript thermodynamics, sampling, an independent thermodynamic implementation, and two learned models; kinetic, pseudoknot, G4 and MFE-only extensions are outside this focused equilibrium comparison. RNAplfold CLI 2.4.7 and bindings 2.7.2 are a version-different parity check, not independent evidence. Experiments are annotations in the companion comparison, not SHAPE pseudoenergies.
