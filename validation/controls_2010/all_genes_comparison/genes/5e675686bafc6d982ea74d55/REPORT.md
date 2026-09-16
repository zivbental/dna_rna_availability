# YCL016C
Status: ok. Length: 1312 nt. Measured usable bases: 553. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 553 | 0.4122 | 0.3801 |
| rnafold | ok | 553 | 0.2866 | 0.2869 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 67 | 0.0702 | -0.0725 |
| seed_p | 67 | -0.4054 | -0.3794 |
| seed_p_vs_seed_pars | 63 | -0.5576 | -0.4990 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
