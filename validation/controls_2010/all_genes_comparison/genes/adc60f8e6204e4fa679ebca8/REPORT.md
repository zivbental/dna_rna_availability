# YLR353W
Status: ok. Length: 2017 nt. Measured usable bases: 784. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 784 | 0.3838 | 0.3723 |
| rnafold | ok | 784 | 0.3294 | 0.3222 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 57 | -0.2616 | -0.2376 |
| seed_p | 57 | -0.0298 | 0.1304 |
| seed_p_vs_seed_pars | 44 | 0.0449 | 0.1058 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
