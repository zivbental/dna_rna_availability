# YLR300W
Status: ok. Length: 1669 nt. Measured usable bases: 1504. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1504 | 0.3341 | 0.3231 |
| rnafold | ok | 1504 | 0.2834 | 0.2890 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1416 | -0.1453 | -0.1089 |
| seed_p | 1416 | -0.3060 | -0.2545 |
| seed_p_vs_seed_pars | 1339 | -0.4422 | -0.3548 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
