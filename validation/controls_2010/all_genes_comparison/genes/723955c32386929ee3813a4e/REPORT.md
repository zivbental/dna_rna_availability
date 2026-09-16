# YOR045W
Status: ok. Length: 379 nt. Measured usable bases: 294. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 294 | 0.1731 | 0.1296 |
| rnafold | ok | 294 | 0.2556 | 0.2151 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 229 | 0.2497 | 0.2834 |
| seed_p | 229 | -0.0246 | -0.0061 |
| seed_p_vs_seed_pars | 195 | -0.3239 | -0.1763 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
