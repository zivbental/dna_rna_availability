# YEL003W
Status: ok. Length: 461 nt. Measured usable bases: 216. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 216 | 0.3691 | 0.3536 |
| rnafold | ok | 216 | 0.3877 | 0.4117 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 94 | -0.3728 | -0.5506 |
| seed_p | 94 | -0.6535 | -0.6565 |
| seed_p_vs_seed_pars | 73 | -0.6870 | -0.7245 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
