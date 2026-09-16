# YAR014C
Status: ok. Length: 2443 nt. Measured usable bases: 980.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 980 | 0.3709 | 0.3751 |
| rnafold | ok | 980 | 0.2907 | 0.3180 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 98 | 0.0886 | 0.0390 |
| seed_p | 98 | 0.3685 | 0.2192 |
| seed_p_vs_seed_pars | 84 | 0.4609 | 0.4982 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
