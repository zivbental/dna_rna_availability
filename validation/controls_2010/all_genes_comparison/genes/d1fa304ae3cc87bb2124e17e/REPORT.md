# YMR143W
Status: ok. Length: 545 nt. Measured usable bases: 332. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 332 | 0.3553 | 0.3396 |
| rnafold | ok | 332 | 0.1848 | 0.1911 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 163 | 0.2677 | 0.2089 |
| seed_p | 163 | -0.3783 | -0.1146 |
| seed_p_vs_seed_pars | 130 | -0.4125 | -0.2729 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
