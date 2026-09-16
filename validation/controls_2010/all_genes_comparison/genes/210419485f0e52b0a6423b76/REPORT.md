# YML012W
Status: ok. Length: 810 nt. Measured usable bases: 611. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 611 | 0.3580 | 0.3371 |
| rnafold | ok | 611 | 0.3026 | 0.3277 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 581 | 0.0128 | 0.0036 |
| seed_p | 581 | -0.1468 | -0.0681 |
| seed_p_vs_seed_pars | 478 | -0.2843 | -0.1526 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
