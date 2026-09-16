# YHR183W
Status: ok. Length: 1669 nt. Measured usable bases: 1482. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1482 | 0.2965 | 0.2723 |
| rnafold | ok | 1482 | 0.2523 | 0.2304 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1455 | -0.0819 | -0.1005 |
| seed_p | 1455 | -0.1123 | -0.0747 |
| seed_p_vs_seed_pars | 1293 | -0.2405 | -0.1015 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
