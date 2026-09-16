# YJR015W
Status: ok. Length: 1666 nt. Measured usable bases: 1256. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1256 | 0.2672 | 0.2462 |
| rnafold | ok | 1256 | 0.2157 | 0.2073 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 972 | 0.0561 | 0.0667 |
| seed_p | 972 | -0.1790 | -0.1152 |
| seed_p_vs_seed_pars | 851 | -0.3180 | -0.2076 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
