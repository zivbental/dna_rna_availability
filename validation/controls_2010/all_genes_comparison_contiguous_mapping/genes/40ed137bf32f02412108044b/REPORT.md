# YBL095W
Status: ok. Length: 933 nt. Measured usable bases: 374.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 374 | 0.3985 | 0.3942 |
| rnafold | ok | 374 | 0.2824 | 0.2952 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 27 | -0.7127 | -0.8801 |
| seed_p | 27 | 0.2091 | 0.6259 |
| seed_p_vs_seed_pars | 7 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
