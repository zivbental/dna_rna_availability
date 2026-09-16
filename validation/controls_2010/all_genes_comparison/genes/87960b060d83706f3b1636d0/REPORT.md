# YMR171C
Status: ok. Length: 2064 nt. Measured usable bases: 981. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 981 | 0.3060 | 0.3075 |
| rnafold | ok | 981 | 0.2447 | 0.2482 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 134 | -0.2436 | -0.6013 |
| seed_p | 134 | -0.5605 | -0.5782 |
| seed_p_vs_seed_pars | 113 | -0.3811 | -0.4567 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
