# YDR196C
Status: ok. Length: 829 nt. Measured usable bases: 375. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 375 | 0.3754 | 0.3785 |
| rnafold | ok | 375 | 0.3286 | 0.3346 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 35 | 0.2244 | 0.1041 |
| seed_p | 35 | 0.6086 | 0.4054 |
| seed_p_vs_seed_pars | 14 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
