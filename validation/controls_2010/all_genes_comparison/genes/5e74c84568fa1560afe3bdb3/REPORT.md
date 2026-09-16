# YBR094W
Status: ok. Length: 2409 nt. Measured usable bases: 925. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 925 | 0.2577 | 0.2661 |
| rnafold | ok | 925 | 0.2680 | 0.2646 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 35 | -0.2779 | -0.2508 |
| seed_p | 35 | -0.6435 | -0.5466 |
| seed_p_vs_seed_pars | 24 | -0.7993 | -0.4582 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
