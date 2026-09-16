# YBR175W
Status: ok. Length: 1008 nt. Measured usable bases: 649. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 649 | 0.2474 | 0.2473 |
| rnafold | ok | 649 | 0.2549 | 0.2555 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 338 | -0.1302 | 0.0345 |
| seed_p | 338 | -0.1905 | -0.1697 |
| seed_p_vs_seed_pars | 266 | -0.3196 | -0.3394 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
