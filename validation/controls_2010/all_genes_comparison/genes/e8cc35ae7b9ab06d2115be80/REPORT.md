# YCL044C
Status: ok. Length: 1428 nt. Measured usable bases: 649. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 649 | 0.2781 | 0.2785 |
| rnafold | ok | 649 | 0.1526 | 0.1684 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 91 | 0.0006 | 0.1084 |
| seed_p | 91 | 0.0882 | 0.0605 |
| seed_p_vs_seed_pars | 65 | 0.1290 | 0.0981 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
