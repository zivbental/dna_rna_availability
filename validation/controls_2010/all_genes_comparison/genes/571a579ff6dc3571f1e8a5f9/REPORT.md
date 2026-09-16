# YJR103W
Status: ok. Length: 1896 nt. Measured usable bases: 1118. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1118 | 0.3099 | 0.2885 |
| rnafold | ok | 1118 | 0.2848 | 0.2744 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 534 | 0.1914 | -0.0056 |
| seed_p | 534 | -0.0827 | -0.0569 |
| seed_p_vs_seed_pars | 433 | -0.1686 | -0.0925 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
