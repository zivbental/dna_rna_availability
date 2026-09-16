# YHR196W
Status: ok. Length: 1831 nt. Measured usable bases: 805. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 805 | 0.3622 | 0.3572 |
| rnafold | ok | 805 | 0.3418 | 0.3471 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 111 | -0.2494 | -0.3521 |
| seed_p | 111 | -0.0412 | -0.1384 |
| seed_p_vs_seed_pars | 71 | -0.0237 | -0.0302 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
