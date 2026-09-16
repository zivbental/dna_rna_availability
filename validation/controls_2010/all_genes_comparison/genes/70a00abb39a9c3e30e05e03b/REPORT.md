# YGR208W
Status: ok. Length: 1022 nt. Measured usable bases: 660. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 660 | 0.4062 | 0.4029 |
| rnafold | ok | 660 | 0.3110 | 0.3295 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 330 | -0.0539 | 0.0082 |
| seed_p | 330 | -0.1537 | -0.0431 |
| seed_p_vs_seed_pars | 270 | -0.2585 | -0.2323 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
