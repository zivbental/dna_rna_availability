# YOR085W
Status: ok. Length: 1383 nt. Measured usable bases: 778. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 778 | 0.1498 | 0.1401 |
| rnafold | ok | 778 | 0.1862 | 0.1891 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 449 | 0.1530 | 0.1397 |
| seed_p | 449 | 0.1311 | 0.1654 |
| seed_p_vs_seed_pars | 306 | 0.1784 | 0.1367 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
