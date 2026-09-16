# YLR413W
Status: ok. Length: 2225 nt. Measured usable bases: 1880. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1880 | 0.2796 | 0.2693 |
| rnafold | ok | 1880 | 0.2287 | 0.2270 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1832 | -0.1333 | -0.1782 |
| seed_p | 1832 | -0.2780 | -0.2348 |
| seed_p_vs_seed_pars | 1526 | -0.3665 | -0.3135 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
