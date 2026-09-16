# YBR106W
Status: ok. Length: 753 nt. Measured usable bases: 705.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 705 | 0.3035 | 0.2887 |
| rnafold | ok | 705 | 0.2772 | 0.2525 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 694 | 0.0321 | -0.0745 |
| seed_p | 694 | 0.0104 | 0.0608 |
| seed_p_vs_seed_pars | 672 | 0.0067 | 0.1059 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
