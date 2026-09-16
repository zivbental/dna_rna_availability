# YPR010C
Status: ok. Length: 3789 nt. Measured usable bases: 2918. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2918 | 0.3187 | 0.3076 |
| rnafold | ok | 2918 | 0.2330 | 0.2246 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 2014 | 0.0287 | -0.1256 |
| seed_p | 2014 | -0.2499 | -0.2259 |
| seed_p_vs_seed_pars | 1619 | -0.3287 | -0.3078 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
