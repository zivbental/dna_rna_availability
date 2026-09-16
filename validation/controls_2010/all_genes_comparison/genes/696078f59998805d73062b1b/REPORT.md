# YMR183C
Status: ok. Length: 1043 nt. Measured usable bases: 663. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 663 | 0.3030 | 0.2931 |
| rnafold | ok | 663 | 0.2970 | 0.2934 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 291 | 0.2297 | 0.1566 |
| seed_p | 291 | 0.0616 | 0.0145 |
| seed_p_vs_seed_pars | 230 | -0.0231 | -0.1304 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
