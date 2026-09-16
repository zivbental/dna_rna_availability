# YPR020W
Status: ok. Length: 494 nt. Measured usable bases: 220. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 220 | 0.3089 | 0.2717 |
| rnafold | ok | 220 | 0.3109 | 0.2691 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 48 | -0.0007 | 0.0674 |
| seed_p | 48 | -0.3212 | -0.1785 |
| seed_p_vs_seed_pars | 30 | -0.6206 | -0.6455 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
