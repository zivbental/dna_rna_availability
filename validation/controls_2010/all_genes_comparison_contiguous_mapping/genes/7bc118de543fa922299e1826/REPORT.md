# YBR029C
Status: ok. Length: 2180 nt. Measured usable bases: 963.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 963 | 0.2752 | 0.2614 |
| rnafold | ok | 963 | 0.1906 | 0.1803 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 346 | -0.1804 | -0.0940 |
| seed_p | 346 | -0.2457 | -0.1937 |
| seed_p_vs_seed_pars | 276 | -0.3839 | -0.2915 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
