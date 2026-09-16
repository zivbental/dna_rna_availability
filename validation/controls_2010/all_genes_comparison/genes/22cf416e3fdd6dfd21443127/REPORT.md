# YFR010W
Status: ok. Length: 1675 nt. Measured usable bases: 810. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 810 | 0.3084 | 0.2971 |
| rnafold | ok | 810 | 0.2595 | 0.2562 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 193 | -0.1086 | 0.0471 |
| seed_p | 193 | -0.0117 | 0.0761 |
| seed_p_vs_seed_pars | 125 | -0.4394 | -0.2892 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
