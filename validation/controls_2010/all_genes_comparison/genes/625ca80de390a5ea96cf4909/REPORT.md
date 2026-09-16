# YHR083W
Status: ok. Length: 1086 nt. Measured usable bases: 755. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 755 | 0.3607 | 0.3400 |
| rnafold | ok | 755 | 0.3932 | 0.3740 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 380 | -0.1255 | -0.3100 |
| seed_p | 380 | -0.2520 | -0.3227 |
| seed_p_vs_seed_pars | 300 | -0.4599 | -0.4802 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
