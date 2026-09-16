# YOR271C
Status: ok. Length: 1106 nt. Measured usable bases: 799. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 799 | 0.3532 | 0.3426 |
| rnafold | ok | 799 | 0.2873 | 0.2754 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 570 | -0.0685 | -0.1917 |
| seed_p | 570 | -0.2809 | -0.3583 |
| seed_p_vs_seed_pars | 416 | -0.3397 | -0.3907 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
