# YBL054W
Status: ok. Length: 1874 nt. Measured usable bases: 853.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 853 | 0.3321 | 0.3427 |
| rnafold | ok | 853 | 0.2867 | 0.2895 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 159 | -0.0071 | -0.1460 |
| seed_p | 159 | -0.2483 | -0.2452 |
| seed_p_vs_seed_pars | 108 | -0.4341 | -0.4527 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
