# YHL034C
Status: ok. Length: 1126 nt. Measured usable bases: 796. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 796 | 0.3220 | 0.3257 |
| rnafold | ok | 796 | 0.2966 | 0.3059 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 485 | 0.1188 | 0.0473 |
| seed_p | 485 | -0.0032 | 0.0880 |
| seed_p_vs_seed_pars | 412 | -0.0885 | -0.0104 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
