# YFL009W
Status: ok. Length: 2606 nt. Measured usable bases: 1075. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1075 | 0.3368 | 0.3287 |
| rnafold | ok | 1075 | 0.3196 | 0.3283 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 166 | -0.0757 | -0.1376 |
| seed_p | 166 | -0.0520 | -0.0289 |
| seed_p_vs_seed_pars | 117 | 0.0809 | -0.0388 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
