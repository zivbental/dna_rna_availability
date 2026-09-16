# YGL236C
Status: ok. Length: 2066 nt. Measured usable bases: 911. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 911 | 0.3253 | 0.3192 |
| rnafold | ok | 911 | 0.2672 | 0.2713 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 89 | -0.5373 | -0.8537 |
| seed_p | 89 | -0.3192 | -0.3778 |
| seed_p_vs_seed_pars | 77 | -0.3760 | -0.5123 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
