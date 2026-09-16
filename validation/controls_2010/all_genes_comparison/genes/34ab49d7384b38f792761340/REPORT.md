# YLR427W
Status: ok. Length: 2272 nt. Measured usable bases: 848. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 848 | 0.3580 | 0.3475 |
| rnafold | ok | 848 | 0.3041 | 0.2873 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 80 | 0.2514 | 0.3599 |
| seed_p | 80 | -0.4800 | -0.2500 |
| seed_p_vs_seed_pars | 71 | -0.5890 | -0.6596 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
