# YNL022C
Status: ok. Length: 1552 nt. Measured usable bases: 640. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 640 | 0.3717 | 0.3720 |
| rnafold | ok | 640 | 0.3416 | 0.3451 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 31 | -0.0244 | 0.0040 |
| seed_p | 31 | -0.4000 | -0.5692 |
| seed_p_vs_seed_pars | 24 | -0.5953 | -0.6306 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
