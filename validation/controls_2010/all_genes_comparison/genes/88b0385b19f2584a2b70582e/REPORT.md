# YMR158W
Status: ok. Length: 596 nt. Measured usable bases: 256. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 256 | 0.3826 | 0.3527 |
| rnafold | ok | 256 | 0.4176 | 0.3906 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 36 | -0.5464 | -0.4722 |
| seed_p | 36 | -0.4750 | -0.4629 |
| seed_p_vs_seed_pars | 32 | -0.6214 | -0.7254 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
