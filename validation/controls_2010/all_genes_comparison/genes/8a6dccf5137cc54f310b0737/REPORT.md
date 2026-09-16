# YOL003C
Status: ok. Length: 1262 nt. Measured usable bases: 716. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 716 | 0.3442 | 0.3297 |
| rnafold | ok | 716 | 0.3289 | 0.3290 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 233 | -0.2739 | -0.3759 |
| seed_p | 233 | -0.1707 | -0.0587 |
| seed_p_vs_seed_pars | 155 | -0.2639 | -0.3031 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
