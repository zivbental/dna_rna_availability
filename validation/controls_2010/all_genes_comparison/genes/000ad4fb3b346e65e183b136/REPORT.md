# YBR151W
Status: ok. Length: 1232 nt. Measured usable bases: 791. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 791 | 0.3395 | 0.3248 |
| rnafold | ok | 791 | 0.2829 | 0.2678 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 398 | -0.2034 | -0.1286 |
| seed_p | 398 | 0.0293 | 0.0941 |
| seed_p_vs_seed_pars | 300 | -0.2582 | -0.3178 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
