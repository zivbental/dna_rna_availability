# RDN5-6
Status: ok. Length: 121 nt. Measured usable bases: 97.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 97 | 0.2104 | 0.2098 |
| rnafold | ok | 97 | 0.2104 | 0.2098 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 82 | -0.0010 | 0.1579 |
| seed_p | 82 | -0.0342 | -0.0544 |
| seed_p_vs_seed_pars | 82 | -0.3383 | -0.2359 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
