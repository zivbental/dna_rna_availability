# YLR287C
Status: ok. Length: 1370 nt. Measured usable bases: 694. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 694 | 0.3254 | 0.3261 |
| rnafold | ok | 694 | 0.3175 | 0.3059 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 106 | -0.1992 | -0.1231 |
| seed_p | 106 | -0.0258 | -0.0228 |
| seed_p_vs_seed_pars | 69 | -0.0481 | -0.0791 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
