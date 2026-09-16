# YER057C
Status: ok. Length: 479 nt. Measured usable bases: 425. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 425 | 0.3254 | 0.2994 |
| rnafold | ok | 425 | 0.2597 | 0.2583 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 435 | -0.1808 | -0.3424 |
| seed_p | 435 | -0.3655 | -0.3133 |
| seed_p_vs_seed_pars | 383 | -0.4256 | -0.4047 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
