# YGL017W
Status: ok. Length: 1612 nt. Measured usable bases: 612. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 612 | 0.4177 | 0.4238 |
| rnafold | ok | 612 | 0.3115 | 0.3129 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 30 | -0.6548 | -0.5871 |
| seed_p | 30 | -0.0072 | -0.1542 |
| seed_p_vs_seed_pars | 18 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
