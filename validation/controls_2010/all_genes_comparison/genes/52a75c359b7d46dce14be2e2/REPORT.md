# YGL172W
Status: ok. Length: 1538 nt. Measured usable bases: 917. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 917 | 0.3009 | 0.3020 |
| rnafold | ok | 917 | 0.2753 | 0.2753 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 321 | -0.2272 | -0.2470 |
| seed_p | 321 | -0.2744 | -0.4625 |
| seed_p_vs_seed_pars | 232 | -0.4314 | -0.5751 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
