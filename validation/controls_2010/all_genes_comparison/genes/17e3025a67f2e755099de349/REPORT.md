# YOR196C
Status: ok. Length: 1406 nt. Measured usable bases: 669. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 669 | 0.3950 | 0.3768 |
| rnafold | ok | 669 | 0.2822 | 0.2849 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 43 | -0.1234 | -0.0984 |
| seed_p | 43 | -0.8164 | -0.6257 |
| seed_p_vs_seed_pars | 23 | -0.8792 | -0.7029 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
