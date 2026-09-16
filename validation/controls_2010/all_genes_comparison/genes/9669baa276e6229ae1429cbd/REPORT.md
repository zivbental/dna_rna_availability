# YOR202W
Status: ok. Length: 755 nt. Measured usable bases: 501. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 501 | 0.3206 | 0.3070 |
| rnafold | ok | 501 | 0.3327 | 0.3309 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 247 | -0.3310 | -0.5950 |
| seed_p | 247 | -0.5801 | -0.6051 |
| seed_p_vs_seed_pars | 214 | -0.3338 | -0.3239 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
