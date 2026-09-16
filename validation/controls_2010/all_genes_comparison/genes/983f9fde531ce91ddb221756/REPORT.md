# YKL084W
Status: ok. Length: 516 nt. Measured usable bases: 235. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 235 | 0.3045 | 0.2419 |
| rnafold | ok | 235 | 0.3651 | 0.3248 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 54 | -0.2873 | -0.0158 |
| seed_p | 54 | -0.2936 | -0.2404 |
| seed_p_vs_seed_pars | 36 | -0.5620 | -0.5112 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
