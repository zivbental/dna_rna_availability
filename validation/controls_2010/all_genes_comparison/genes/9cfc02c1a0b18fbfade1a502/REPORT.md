# YDL075W
Status: ok. Length: 433 nt. Measured usable bases: 278. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 278 | 0.3869 | 0.3559 |
| rnafold | ok | 278 | 0.3281 | 0.2925 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 169 | -0.0833 | -0.2773 |
| seed_p | 169 | -0.5356 | -0.4284 |
| seed_p_vs_seed_pars | 139 | -0.7762 | -0.2786 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
