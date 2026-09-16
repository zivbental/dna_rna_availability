# YIL103W
Status: ok. Length: 1379 nt. Measured usable bases: 694. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 694 | 0.2881 | 0.2822 |
| rnafold | ok | 694 | 0.2254 | 0.2153 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 143 | 0.2086 | 0.3967 |
| seed_p | 143 | 0.1699 | 0.1051 |
| seed_p_vs_seed_pars | 92 | 0.0992 | -0.0112 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
