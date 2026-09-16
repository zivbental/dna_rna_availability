# YER021W
Status: ok. Length: 1700 nt. Measured usable bases: 1248. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1248 | 0.3324 | 0.3338 |
| rnafold | ok | 1248 | 0.2501 | 0.2635 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 907 | -0.2595 | -0.3256 |
| seed_p | 907 | -0.2745 | -0.2829 |
| seed_p_vs_seed_pars | 752 | -0.1859 | -0.2281 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
