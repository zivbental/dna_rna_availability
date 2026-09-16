# YBR077C
Status: ok. Length: 814 nt. Measured usable bases: 506.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 506 | 0.4336 | 0.4307 |
| rnafold | ok | 506 | 0.3874 | 0.3693 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 263 | -0.1695 | -0.3279 |
| seed_p | 263 | -0.3504 | -0.4303 |
| seed_p_vs_seed_pars | 214 | -0.4004 | -0.3475 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
