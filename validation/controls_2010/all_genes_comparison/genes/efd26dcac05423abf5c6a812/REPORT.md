# YIR011C
Status: ok. Length: 1063 nt. Measured usable bases: 463. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 463 | 0.3312 | 0.3275 |
| rnafold | ok | 463 | 0.3330 | 0.3275 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 67 | 0.0072 | 0.3406 |
| seed_p | 67 | 0.0784 | 0.1489 |
| seed_p_vs_seed_pars | 62 | -0.0977 | -0.0901 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
