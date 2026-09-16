# YJR117W
Status: ok. Length: 1494 nt. Measured usable bases: 1037. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1037 | 0.1980 | 0.1974 |
| rnafold | ok | 1037 | 0.1641 | 0.1466 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 574 | -0.1578 | -0.2342 |
| seed_p | 574 | -0.1331 | -0.1617 |
| seed_p_vs_seed_pars | 453 | -0.0445 | -0.2161 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
