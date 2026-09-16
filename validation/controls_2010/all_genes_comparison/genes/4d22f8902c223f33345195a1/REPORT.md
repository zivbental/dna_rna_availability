# YOR359W
Status: ok. Length: 1923 nt. Measured usable bases: 710. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 710 | 0.1852 | 0.1720 |
| rnafold | ok | 710 | 0.1484 | 0.1352 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 36 | -0.1144 | -0.4068 |
| seed_p | 36 | 0.1522 | 0.1499 |
| seed_p_vs_seed_pars | 27 | 0.0632 | 0.1093 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
