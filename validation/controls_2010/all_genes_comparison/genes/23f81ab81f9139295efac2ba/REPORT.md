# YHR039C
Status: ok. Length: 2097 nt. Measured usable bases: 1508. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1508 | 0.2824 | 0.2728 |
| rnafold | ok | 1508 | 0.2585 | 0.2488 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1026 | 0.0469 | -0.0259 |
| seed_p | 1026 | -0.1241 | -0.1016 |
| seed_p_vs_seed_pars | 782 | -0.2791 | -0.2545 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
