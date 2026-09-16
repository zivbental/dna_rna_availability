# YDR337W
Status: ok. Length: 963 nt. Measured usable bases: 331. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 331 | 0.3080 | 0.3026 |
| rnafold | ok | 331 | 0.3641 | 0.3533 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 30 | -0.7202 | -0.6953 |
| seed_p | 30 | -0.7533 | -0.8102 |
| seed_p_vs_seed_pars | 13 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
