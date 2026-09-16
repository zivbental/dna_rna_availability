# YJR041C
Status: ok. Length: 3786 nt. Measured usable bases: 1232. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1232 | 0.3337 | 0.3174 |
| rnafold | ok | 1232 | 0.2139 | 0.2273 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 62 | 0.3886 | 0.1523 |
| seed_p | 62 | -0.0707 | 0.0009 |
| seed_p_vs_seed_pars | 38 | -0.4034 | -0.3377 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
