# YHR175W
Status: ok. Length: 774 nt. Measured usable bases: 441. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 441 | 0.1983 | 0.1730 |
| rnafold | ok | 441 | 0.1330 | 0.1516 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 224 | -0.0182 | -0.1689 |
| seed_p | 224 | 0.0692 | -0.0429 |
| seed_p_vs_seed_pars | 213 | -0.0779 | -0.2181 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
