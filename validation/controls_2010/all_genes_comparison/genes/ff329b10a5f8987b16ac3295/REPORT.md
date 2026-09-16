# YDR374W-A
Status: ok. Length: 477 nt. Measured usable bases: 225. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 225 | 0.3808 | 0.3901 |
| rnafold | ok | 225 | 0.3328 | 0.3523 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 46 | 0.2529 | 0.4112 |
| seed_p | 46 | -0.1858 | -0.4477 |
| seed_p_vs_seed_pars | 42 | -0.7397 | -0.8475 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
