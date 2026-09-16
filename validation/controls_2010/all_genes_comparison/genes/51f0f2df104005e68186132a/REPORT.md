# YDL131W
Status: ok. Length: 1479 nt. Measured usable bases: 578. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 578 | 0.3035 | 0.2883 |
| rnafold | ok | 578 | 0.2565 | 0.2404 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 254 | -0.1452 | -0.0190 |
| seed_p | 254 | -0.3392 | -0.2876 |
| seed_p_vs_seed_pars | 199 | -0.2486 | -0.3052 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
