# YLL001W
Status: ok. Length: 2479 nt. Measured usable bases: 1046. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1046 | 0.3483 | 0.3461 |
| rnafold | ok | 1046 | 0.2888 | 0.2990 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 166 | -0.3948 | -0.3193 |
| seed_p | 166 | -0.1990 | -0.1850 |
| seed_p_vs_seed_pars | 137 | -0.2910 | -0.3267 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
