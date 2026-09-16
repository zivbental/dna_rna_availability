# YGR125W
Status: ok. Length: 3196 nt. Measured usable bases: 1079. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1079 | 0.3181 | 0.3009 |
| rnafold | ok | 1079 | 0.2645 | 0.2492 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 56 | -0.3976 | -0.2996 |
| seed_p | 56 | -0.0268 | -0.2275 |
| seed_p_vs_seed_pars | 44 | 0.0774 | -0.2057 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
