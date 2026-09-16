# YNL247W
Status: ok. Length: 2433 nt. Measured usable bases: 1525. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1525 | 0.2875 | 0.2803 |
| rnafold | ok | 1525 | 0.2188 | 0.2314 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 570 | -0.0353 | -0.0047 |
| seed_p | 570 | 0.0124 | -0.0524 |
| seed_p_vs_seed_pars | 447 | -0.0360 | -0.1276 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
