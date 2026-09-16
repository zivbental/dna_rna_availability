# YMR199W
Status: ok. Length: 1932 nt. Measured usable bases: 784. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 784 | 0.2402 | 0.2324 |
| rnafold | ok | 784 | 0.1481 | 0.1439 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 56 | -0.2541 | -0.0035 |
| seed_p | 56 | -0.5379 | -0.6157 |
| seed_p_vs_seed_pars | 38 | -0.0918 | -0.0090 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
