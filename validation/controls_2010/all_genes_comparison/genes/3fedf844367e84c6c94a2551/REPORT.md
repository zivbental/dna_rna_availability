# YDR251W
Status: ok. Length: 2907 nt. Measured usable bases: 1196. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1196 | 0.2971 | 0.2942 |
| rnafold | ok | 1196 | 0.2078 | 0.2254 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 121 | 0.1454 | 0.1256 |
| seed_p | 121 | 0.3463 | 0.4771 |
| seed_p_vs_seed_pars | 78 | 0.3967 | 0.4464 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
