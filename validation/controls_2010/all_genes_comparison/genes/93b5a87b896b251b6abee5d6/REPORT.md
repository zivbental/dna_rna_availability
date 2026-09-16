# YGR148C
Status: ok. Length: 1023 nt. Measured usable bases: 437. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 437 | 0.3399 | 0.3379 |
| rnafold | ok | 437 | 0.2303 | 0.2268 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 180 | -0.1763 | 0.0415 |
| seed_p | 180 | -0.2411 | -0.2003 |
| seed_p_vs_seed_pars | 155 | -0.2771 | -0.1702 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
