# YBR034C
Status: ok. Length: 1223 nt. Measured usable bases: 832. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 832 | 0.2903 | 0.2431 |
| rnafold | ok | 832 | 0.2888 | 0.2514 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 481 | -0.1356 | 0.1188 |
| seed_p | 481 | -0.0234 | 0.0288 |
| seed_p_vs_seed_pars | 380 | -0.1306 | -0.0750 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
