# YBR089C-A
Status: ok. Length: 873 nt. Measured usable bases: 337.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 337 | 0.3394 | 0.3325 |
| rnafold | ok | 337 | 0.2818 | 0.2793 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 174 | -0.1614 | 0.0116 |
| seed_p | 174 | -0.2498 | -0.1379 |
| seed_p_vs_seed_pars | 142 | -0.5286 | -0.4903 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
