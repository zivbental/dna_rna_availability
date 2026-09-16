# YLR303W
Status: ok. Length: 1335 nt. Measured usable bases: 1145. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1145 | 0.2958 | 0.2859 |
| rnafold | ok | 1145 | 0.2691 | 0.2646 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1072 | -0.0413 | -0.0965 |
| seed_p | 1072 | -0.2000 | -0.1731 |
| seed_p_vs_seed_pars | 950 | -0.3299 | -0.2601 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
