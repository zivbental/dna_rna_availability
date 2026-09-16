# YDR452W
Status: ok. Length: 2215 nt. Measured usable bases: 1212. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1212 | 0.3108 | 0.3081 |
| rnafold | ok | 1212 | 0.2566 | 0.2597 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 328 | 0.0874 | 0.2213 |
| seed_p | 328 | 0.1362 | 0.1836 |
| seed_p_vs_seed_pars | 206 | 0.0281 | 0.1383 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
