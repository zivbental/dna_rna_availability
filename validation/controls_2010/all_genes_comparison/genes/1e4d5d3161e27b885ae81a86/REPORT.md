# YHR029C
Status: ok. Length: 885 nt. Measured usable bases: 390. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 390 | 0.3732 | 0.3551 |
| rnafold | ok | 390 | 0.2878 | 0.2746 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 28 | 0.6948 | 0.8151 |
| seed_p | 28 | 0.0181 | 0.2722 |
| seed_p_vs_seed_pars | 21 | 0.7794 | 0.5680 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
