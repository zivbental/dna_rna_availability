# YIL114C
Status: ok. Length: 931 nt. Measured usable bases: 561. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 561 | 0.3323 | 0.3075 |
| rnafold | ok | 561 | 0.3132 | 0.3214 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 242 | 0.0787 | 0.0517 |
| seed_p | 242 | -0.0994 | -0.0513 |
| seed_p_vs_seed_pars | 190 | -0.4675 | -0.3594 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
