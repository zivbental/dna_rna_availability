# YKL035W
Status: ok. Length: 1742 nt. Measured usable bases: 1419. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1419 | 0.3062 | 0.2952 |
| rnafold | ok | 1419 | 0.2495 | 0.2542 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1246 | -0.0985 | -0.0456 |
| seed_p | 1246 | -0.2285 | -0.1754 |
| seed_p_vs_seed_pars | 1003 | -0.3627 | -0.3297 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
