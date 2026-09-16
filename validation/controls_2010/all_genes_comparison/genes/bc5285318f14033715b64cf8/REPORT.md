# YLR134W
Status: ok. Length: 1929 nt. Measured usable bases: 640. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 640 | 0.3156 | 0.3016 |
| rnafold | ok | 640 | 0.2716 | 0.2558 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 27 | -0.0299 | 0.1566 |
| seed_p | 27 | 0.1179 | -0.2389 |
| seed_p_vs_seed_pars | 24 | -0.3299 | -0.3757 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
