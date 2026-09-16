# YBL091C
Status: ok. Length: 1367 nt. Measured usable bases: 972. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 972 | 0.3618 | 0.3459 |
| rnafold | ok | 972 | 0.3104 | 0.2942 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 640 | -0.3604 | -0.2638 |
| seed_p | 640 | -0.0484 | -0.0932 |
| seed_p_vs_seed_pars | 503 | -0.1316 | -0.1701 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
