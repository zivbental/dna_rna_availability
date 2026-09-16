# YER001W
Status: ok. Length: 2751 nt. Measured usable bases: 1502. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1502 | 0.3128 | 0.3051 |
| rnafold | ok | 1502 | 0.2648 | 0.2604 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 514 | -0.1459 | -0.3633 |
| seed_p | 514 | -0.4444 | -0.4494 |
| seed_p_vs_seed_pars | 374 | -0.6113 | -0.5933 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
