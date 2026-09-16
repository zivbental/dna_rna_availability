# YBL032W
Status: ok. Length: 1395 nt. Measured usable bases: 1032. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1032 | 0.3425 | 0.3345 |
| rnafold | ok | 1032 | 0.3678 | 0.3570 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 783 | 0.0788 | -0.2418 |
| seed_p | 783 | -0.2816 | -0.2078 |
| seed_p_vs_seed_pars | 663 | -0.3598 | -0.2510 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
