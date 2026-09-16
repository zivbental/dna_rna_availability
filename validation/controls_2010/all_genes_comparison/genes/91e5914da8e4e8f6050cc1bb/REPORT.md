# YOR367W
Status: ok. Length: 681 nt. Measured usable bases: 342. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 342 | 0.3245 | 0.3267 |
| rnafold | ok | 342 | 0.2374 | 0.2425 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 57 | -0.1236 | 0.2903 |
| seed_p | 57 | -0.2869 | -0.0018 |
| seed_p_vs_seed_pars | 45 | -0.2640 | -0.2172 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
