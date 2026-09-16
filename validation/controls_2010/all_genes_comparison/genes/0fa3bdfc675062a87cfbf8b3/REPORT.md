# YEL009C
Status: ok. Length: 1489 nt. Measured usable bases: 1289. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1289 | 0.2615 | 0.2436 |
| rnafold | ok | 1289 | 0.2546 | 0.2411 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1143 | -0.2240 | -0.1064 |
| seed_p | 1143 | -0.2777 | -0.1477 |
| seed_p_vs_seed_pars | 1037 | -0.3423 | -0.2050 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
