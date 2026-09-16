# YDR463W
Status: ok. Length: 1765 nt. Measured usable bases: 775. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 775 | 0.2655 | 0.2690 |
| rnafold | ok | 775 | 0.2312 | 0.2365 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 116 | 0.1672 | -0.0010 |
| seed_p | 116 | -0.2213 | -0.1338 |
| seed_p_vs_seed_pars | 93 | -0.3244 | -0.1977 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
