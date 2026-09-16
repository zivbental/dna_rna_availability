# YJR126C
Status: ok. Length: 2436 nt. Measured usable bases: 1191. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1191 | 0.3371 | 0.3188 |
| rnafold | ok | 1191 | 0.2230 | 0.2309 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 180 | -0.0809 | -0.1146 |
| seed_p | 180 | -0.0923 | -0.0141 |
| seed_p_vs_seed_pars | 143 | -0.0403 | -0.0657 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
