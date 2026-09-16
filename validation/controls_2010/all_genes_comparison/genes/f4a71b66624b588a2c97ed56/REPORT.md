# YDR127W
Status: ok. Length: 4993 nt. Measured usable bases: 2868. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2868 | 0.3116 | 0.2970 |
| rnafold | ok | 2868 | 0.2284 | 0.2232 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 861 | -0.0964 | -0.1093 |
| seed_p | 861 | -0.2297 | -0.1550 |
| seed_p_vs_seed_pars | 620 | -0.3369 | -0.1851 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
