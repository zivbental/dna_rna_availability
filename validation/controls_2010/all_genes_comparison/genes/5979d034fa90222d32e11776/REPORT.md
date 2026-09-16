# YFR003C
Status: ok. Length: 623 nt. Measured usable bases: 282. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 282 | 0.3529 | 0.3318 |
| rnafold | ok | 282 | 0.3734 | 0.3425 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 43 | -0.1178 | 0.0148 |
| seed_p | 43 | -0.2910 | -0.3917 |
| seed_p_vs_seed_pars | 25 | -0.1944 | -0.4544 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
