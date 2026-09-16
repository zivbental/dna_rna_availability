# YGL003C
Status: ok. Length: 2025 nt. Measured usable bases: 743. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 743 | 0.3330 | 0.3360 |
| rnafold | ok | 743 | 0.2411 | 0.2465 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 53 | -0.1629 | -0.3371 |
| seed_p | 53 | -0.3826 | -0.4705 |
| seed_p_vs_seed_pars | 33 | -0.5142 | -0.5441 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
