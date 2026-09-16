# YOR152C
Status: ok. Length: 1137 nt. Measured usable bases: 461. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 461 | 0.2913 | 0.2905 |
| rnafold | ok | 461 | 0.2676 | 0.2775 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 58 | -0.2474 | 0.1733 |
| seed_p | 58 | -0.1651 | -0.0383 |
| seed_p_vs_seed_pars | 50 | -0.2936 | -0.4759 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
