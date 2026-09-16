# YKL181W
Status: ok. Length: 1553 nt. Measured usable bases: 1361. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1361 | 0.3456 | 0.3358 |
| rnafold | ok | 1361 | 0.2476 | 0.2700 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1306 | -0.0209 | -0.1112 |
| seed_p | 1306 | -0.1139 | -0.1230 |
| seed_p_vs_seed_pars | 1167 | -0.1592 | -0.1597 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
