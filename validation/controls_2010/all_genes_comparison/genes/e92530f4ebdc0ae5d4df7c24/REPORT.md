# YOR293W
Status: ok. Length: 494 nt. Measured usable bases: 318. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 318 | 0.3182 | 0.2997 |
| rnafold | ok | 318 | 0.1605 | 0.1494 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 221 | -0.0129 | -0.0572 |
| seed_p | 221 | -0.4092 | -0.3385 |
| seed_p_vs_seed_pars | 193 | -0.3689 | -0.3882 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
