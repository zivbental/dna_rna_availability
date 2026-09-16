# YPL225W
Status: ok. Length: 601 nt. Measured usable bases: 339. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 339 | 0.2388 | 0.2280 |
| rnafold | ok | 339 | 0.2772 | 0.2684 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 182 | 0.2393 | -0.0072 |
| seed_p | 182 | 0.0299 | -0.0685 |
| seed_p_vs_seed_pars | 130 | 0.1068 | -0.0730 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
