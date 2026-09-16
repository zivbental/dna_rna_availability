# YPL239W
Status: ok. Length: 878 nt. Measured usable bases: 483. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 483 | 0.4118 | 0.4080 |
| rnafold | ok | 483 | 0.4165 | 0.4025 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 143 | -0.1355 | -0.1823 |
| seed_p | 143 | -0.1329 | -0.1258 |
| seed_p_vs_seed_pars | 125 | 0.1064 | 0.1768 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
