# YNL045W
Status: ok. Length: 2084 nt. Measured usable bases: 1350. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1350 | 0.2846 | 0.2636 |
| rnafold | ok | 1350 | 0.2644 | 0.2440 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 528 | 0.0166 | -0.0803 |
| seed_p | 528 | -0.2971 | -0.2441 |
| seed_p_vs_seed_pars | 429 | -0.4147 | -0.3342 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
