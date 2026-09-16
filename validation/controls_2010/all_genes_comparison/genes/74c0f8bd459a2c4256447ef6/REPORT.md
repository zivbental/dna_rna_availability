# YGL246C
Status: ok. Length: 1316 nt. Measured usable bases: 545. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 545 | 0.4036 | 0.3940 |
| rnafold | ok | 545 | 0.3295 | 0.3171 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 45 | -0.3489 | -0.3694 |
| seed_p | 45 | -0.3602 | -0.3159 |
| seed_p_vs_seed_pars | 21 | -0.9331 | -0.8133 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
