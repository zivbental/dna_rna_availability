# YMR221C
Status: ok. Length: 1626 nt. Measured usable bases: 1008. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1008 | 0.1634 | 0.1431 |
| rnafold | ok | 1008 | 0.1358 | 0.1054 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 396 | -0.1115 | -0.1200 |
| seed_p | 396 | -0.1677 | -0.1981 |
| seed_p_vs_seed_pars | 286 | -0.2209 | -0.2185 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
