# YGR185C
Status: ok. Length: 1289 nt. Measured usable bases: 1041. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1041 | 0.3677 | 0.3576 |
| rnafold | ok | 1041 | 0.3257 | 0.3406 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 953 | -0.1887 | -0.2871 |
| seed_p | 953 | -0.1565 | -0.2546 |
| seed_p_vs_seed_pars | 800 | -0.2428 | -0.2895 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
