# YLR109W
Status: ok. Length: 630 nt. Measured usable bases: 580. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 580 | 0.3179 | 0.3262 |
| rnafold | ok | 580 | 0.3212 | 0.3284 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 559 | -0.0664 | -0.1192 |
| seed_p | 559 | -0.0467 | -0.0807 |
| seed_p_vs_seed_pars | 543 | -0.1115 | -0.0694 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
