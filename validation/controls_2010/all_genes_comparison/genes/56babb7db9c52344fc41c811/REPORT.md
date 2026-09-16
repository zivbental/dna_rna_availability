# YDL095W
Status: ok. Length: 2632 nt. Measured usable bases: 2129. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2129 | 0.2547 | 0.2390 |
| rnafold | ok | 2129 | 0.1526 | 0.1409 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1781 | 0.0087 | 0.0386 |
| seed_p | 1781 | -0.1202 | -0.0377 |
| seed_p_vs_seed_pars | 1481 | -0.1460 | -0.0647 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
