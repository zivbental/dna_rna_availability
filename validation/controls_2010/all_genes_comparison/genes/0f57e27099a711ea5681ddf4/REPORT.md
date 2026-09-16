# YDR060W
Status: ok. Length: 3218 nt. Measured usable bases: 1412. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1412 | 0.3402 | 0.3207 |
| rnafold | ok | 1412 | 0.2591 | 0.2448 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 153 | -0.0156 | -0.2198 |
| seed_p | 153 | 0.1001 | 0.1585 |
| seed_p_vs_seed_pars | 108 | -0.0048 | 0.0107 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
