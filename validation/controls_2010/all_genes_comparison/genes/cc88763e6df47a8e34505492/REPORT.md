# YGR261C
Status: ok. Length: 2533 nt. Measured usable bases: 1323. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1323 | 0.2710 | 0.2577 |
| rnafold | ok | 1323 | 0.2431 | 0.2310 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 307 | -0.3064 | -0.0854 |
| seed_p | 307 | -0.2616 | -0.1787 |
| seed_p_vs_seed_pars | 220 | -0.3228 | -0.3264 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
