# YKL151C
Status: ok. Length: 1353 nt. Measured usable bases: 670. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 670 | 0.4179 | 0.4070 |
| rnafold | ok | 670 | 0.3409 | 0.3399 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 185 | -0.1622 | -0.0376 |
| seed_p | 185 | -0.4582 | -0.2968 |
| seed_p_vs_seed_pars | 136 | -0.6673 | -0.5449 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
