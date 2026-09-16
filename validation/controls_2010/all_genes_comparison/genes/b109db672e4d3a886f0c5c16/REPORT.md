# YJL061W
Status: ok. Length: 2324 nt. Measured usable bases: 1072. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1072 | 0.2578 | 0.2400 |
| rnafold | ok | 1072 | 0.2335 | 0.2293 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 84 | -0.1424 | -0.4008 |
| seed_p | 84 | -0.3334 | -0.3160 |
| seed_p_vs_seed_pars | 55 | -0.0281 | 0.1516 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
