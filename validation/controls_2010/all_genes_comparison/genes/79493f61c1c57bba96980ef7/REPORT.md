# YOR103C
Status: ok. Length: 503 nt. Measured usable bases: 355. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 355 | 0.2050 | 0.1891 |
| rnafold | ok | 355 | 0.2194 | 0.2358 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 240 | -0.4666 | -0.5379 |
| seed_p | 240 | -0.4047 | -0.4358 |
| seed_p_vs_seed_pars | 165 | -0.2685 | -0.2524 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
