# YOR357C
Status: ok. Length: 599 nt. Measured usable bases: 251. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 251 | 0.4014 | 0.3637 |
| rnafold | ok | 251 | 0.3533 | 0.3189 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 24 | -0.4687 | -0.3491 |
| seed_p | 24 | 0.4333 | 0.2775 |
| seed_p_vs_seed_pars | 14 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
