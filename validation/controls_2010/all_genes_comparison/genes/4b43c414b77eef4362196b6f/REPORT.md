# YDR435C
Status: ok. Length: 1153 nt. Measured usable bases: 549. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 549 | 0.3730 | 0.3608 |
| rnafold | ok | 549 | 0.3250 | 0.3218 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 137 | -0.3370 | -0.2585 |
| seed_p | 137 | -0.1189 | -0.3730 |
| seed_p_vs_seed_pars | 107 | -0.3124 | -0.5443 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
