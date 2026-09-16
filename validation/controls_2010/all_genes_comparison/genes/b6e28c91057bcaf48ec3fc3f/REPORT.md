# YDR084C
Status: ok. Length: 764 nt. Measured usable bases: 505. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 505 | 0.3851 | 0.3714 |
| rnafold | ok | 505 | 0.3709 | 0.3548 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 238 | -0.3093 | -0.5731 |
| seed_p | 238 | -0.4563 | -0.5219 |
| seed_p_vs_seed_pars | 188 | -0.7745 | -0.7102 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
