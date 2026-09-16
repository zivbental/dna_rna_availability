# YGR147C
Status: ok. Length: 1021 nt. Measured usable bases: 565. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 565 | 0.3015 | 0.2920 |
| rnafold | ok | 565 | 0.2897 | 0.2619 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 238 | -0.0320 | -0.1953 |
| seed_p | 238 | -0.4488 | -0.4515 |
| seed_p_vs_seed_pars | 182 | -0.5062 | -0.4218 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
