# YDR388W
Status: ok. Length: 1615 nt. Measured usable bases: 1116. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1116 | 0.3293 | 0.3135 |
| rnafold | ok | 1116 | 0.2904 | 0.2740 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 619 | 0.0386 | -0.0862 |
| seed_p | 619 | -0.0821 | -0.1285 |
| seed_p_vs_seed_pars | 463 | -0.1361 | -0.3365 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
