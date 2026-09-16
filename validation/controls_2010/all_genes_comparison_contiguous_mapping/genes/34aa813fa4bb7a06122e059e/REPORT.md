# YBR088C
Status: ok. Length: 805 nt. Measured usable bases: 586.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 586 | 0.2261 | 0.2018 |
| rnafold | ok | 586 | 0.2145 | 0.1804 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 400 | 0.0714 | 0.0518 |
| seed_p | 400 | 0.0422 | 0.1289 |
| seed_p_vs_seed_pars | 280 | 0.0354 | 0.0425 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
