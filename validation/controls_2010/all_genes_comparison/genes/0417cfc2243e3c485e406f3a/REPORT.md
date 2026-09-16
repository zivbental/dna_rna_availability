# YHR133C
Status: ok. Length: 1047 nt. Measured usable bases: 708. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 708 | 0.3553 | 0.3406 |
| rnafold | ok | 708 | 0.2729 | 0.2627 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 594 | -0.2323 | -0.2770 |
| seed_p | 594 | -0.3972 | -0.4830 |
| seed_p_vs_seed_pars | 455 | -0.6187 | -0.6991 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
