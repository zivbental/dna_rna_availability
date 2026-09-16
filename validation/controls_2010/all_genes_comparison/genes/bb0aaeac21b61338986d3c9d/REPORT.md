# YGL207W
Status: ok. Length: 3328 nt. Measured usable bases: 1728. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1728 | 0.3449 | 0.3362 |
| rnafold | ok | 1728 | 0.3374 | 0.3187 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 375 | -0.1155 | 0.0316 |
| seed_p | 375 | -0.4794 | -0.3888 |
| seed_p_vs_seed_pars | 278 | -0.5551 | -0.4648 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
