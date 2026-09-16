# YPL266W
Status: ok. Length: 1074 nt. Measured usable bases: 644. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 644 | 0.3570 | 0.3397 |
| rnafold | ok | 644 | 0.2668 | 0.2703 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 311 | 0.1129 | 0.0384 |
| seed_p | 311 | 0.0127 | -0.0226 |
| seed_p_vs_seed_pars | 256 | -0.2082 | -0.2015 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
