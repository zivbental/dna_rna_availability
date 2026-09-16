# YOL059W
Status: ok. Length: 1801 nt. Measured usable bases: 1123. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1123 | 0.2820 | 0.2682 |
| rnafold | ok | 1123 | 0.1816 | 0.1735 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 765 | -0.2290 | -0.1224 |
| seed_p | 765 | -0.1327 | -0.1416 |
| seed_p_vs_seed_pars | 642 | -0.0911 | -0.0917 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
