# YLR034C
Status: ok. Length: 1707 nt. Measured usable bases: 1027. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1027 | 0.2777 | 0.2567 |
| rnafold | ok | 1027 | 0.2565 | 0.2394 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 377 | 0.0488 | -0.0075 |
| seed_p | 377 | -0.2938 | -0.1768 |
| seed_p_vs_seed_pars | 295 | -0.4452 | -0.3179 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
