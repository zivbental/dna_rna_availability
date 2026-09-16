# YBL007C
Status: ok. Length: 3794 nt. Measured usable bases: 2471. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2471 | 0.3270 | 0.3175 |
| rnafold | ok | 2471 | 0.2843 | 0.2856 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1195 | -0.0505 | -0.1233 |
| seed_p | 1195 | -0.2290 | -0.2272 |
| seed_p_vs_seed_pars | 944 | -0.2876 | -0.2616 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
