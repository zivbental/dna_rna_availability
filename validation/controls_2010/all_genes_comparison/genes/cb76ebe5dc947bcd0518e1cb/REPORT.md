# YOR332W
Status: ok. Length: 804 nt. Measured usable bases: 707. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 707 | 0.4107 | 0.4134 |
| rnafold | ok | 707 | 0.3341 | 0.3411 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 685 | -0.1551 | -0.3970 |
| seed_p | 685 | -0.3295 | -0.3775 |
| seed_p_vs_seed_pars | 630 | -0.4519 | -0.4263 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
