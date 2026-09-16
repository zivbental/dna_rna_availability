# YCR072C
Status: ok. Length: 1661 nt. Measured usable bases: 931. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 931 | 0.3085 | 0.2963 |
| rnafold | ok | 931 | 0.2801 | 0.2725 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 328 | -0.3750 | -0.2690 |
| seed_p | 328 | -0.2842 | -0.2266 |
| seed_p_vs_seed_pars | 274 | -0.3799 | -0.3418 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
