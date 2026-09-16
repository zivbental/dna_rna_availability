# YGL014W
Status: ok. Length: 3125 nt. Measured usable bases: 1477. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1477 | 0.2456 | 0.2179 |
| rnafold | ok | 1477 | 0.2012 | 0.1871 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 208 | 0.0988 | 0.0980 |
| seed_p | 208 | 0.0243 | -0.0968 |
| seed_p_vs_seed_pars | 146 | -0.0554 | -0.1267 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
