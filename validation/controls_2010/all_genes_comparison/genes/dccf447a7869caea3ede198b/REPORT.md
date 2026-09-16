# YDL229W
Status: ok. Length: 1982 nt. Measured usable bases: 494. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 494 | 0.2857 | 0.2589 |
| rnafold | ok | 494 | 0.1917 | 0.2007 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 244 | -0.1103 | -0.5285 |
| seed_p | 244 | -0.0785 | -0.3120 |
| seed_p_vs_seed_pars | 224 | -0.0953 | -0.3433 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
