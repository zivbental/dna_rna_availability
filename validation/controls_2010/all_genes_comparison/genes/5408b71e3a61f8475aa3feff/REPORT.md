# YML019W
Status: ok. Length: 1326 nt. Measured usable bases: 876. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 876 | 0.2750 | 0.2714 |
| rnafold | ok | 876 | 0.2378 | 0.2531 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 550 | -0.0223 | -0.0963 |
| seed_p | 550 | -0.0636 | -0.0512 |
| seed_p_vs_seed_pars | 398 | -0.0914 | -0.1411 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
