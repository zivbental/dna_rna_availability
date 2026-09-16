# YNL238W
Status: ok. Length: 2823 nt. Measured usable bases: 1485. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1485 | 0.3190 | 0.3012 |
| rnafold | ok | 1485 | 0.2591 | 0.2604 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 352 | -0.2529 | 0.0608 |
| seed_p | 352 | -0.1104 | 0.1033 |
| seed_p_vs_seed_pars | 256 | -0.0858 | 0.0694 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
