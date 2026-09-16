# YGR234W
Status: ok. Length: 1491 nt. Measured usable bases: 1275. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1275 | 0.2488 | 0.2413 |
| rnafold | ok | 1275 | 0.2273 | 0.2272 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1262 | -0.0648 | -0.1109 |
| seed_p | 1262 | -0.1032 | -0.1516 |
| seed_p_vs_seed_pars | 1170 | -0.2268 | -0.2377 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
