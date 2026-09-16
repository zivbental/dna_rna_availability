# YDL190C
Status: ok. Length: 3197 nt. Measured usable bases: 1460. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1460 | 0.2777 | 0.2760 |
| rnafold | ok | 1460 | 0.2340 | 0.2433 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 195 | -0.1688 | -0.3172 |
| seed_p | 195 | -0.3847 | -0.3830 |
| seed_p_vs_seed_pars | 147 | -0.3393 | -0.3765 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
