# YFR039C
Status: ok. Length: 1692 nt. Measured usable bases: 754. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 754 | 0.3567 | 0.3291 |
| rnafold | ok | 754 | 0.2636 | 0.2390 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 138 | 0.1123 | -0.1052 |
| seed_p | 138 | -0.2254 | 0.1285 |
| seed_p_vs_seed_pars | 86 | -0.5971 | -0.2951 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
