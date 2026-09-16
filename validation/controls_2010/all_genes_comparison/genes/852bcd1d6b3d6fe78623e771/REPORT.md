# YHR028C
Status: ok. Length: 2547 nt. Measured usable bases: 1469. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1469 | 0.2569 | 0.2461 |
| rnafold | ok | 1469 | 0.2315 | 0.2218 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 419 | 0.2273 | 0.1766 |
| seed_p | 419 | -0.1597 | 0.0279 |
| seed_p_vs_seed_pars | 316 | -0.3657 | -0.2727 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
