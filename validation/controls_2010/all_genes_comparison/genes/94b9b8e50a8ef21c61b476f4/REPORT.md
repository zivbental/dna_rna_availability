# YLR088W
Status: ok. Length: 2058 nt. Measured usable bases: 1132. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1132 | 0.2541 | 0.2457 |
| rnafold | ok | 1132 | 0.2123 | 0.2000 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 246 | 0.0540 | -0.1568 |
| seed_p | 246 | -0.0724 | -0.0499 |
| seed_p_vs_seed_pars | 127 | -0.3594 | -0.3461 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
