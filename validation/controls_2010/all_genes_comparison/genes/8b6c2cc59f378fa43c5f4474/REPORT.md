# YHR013C
Status: ok. Length: 843 nt. Measured usable bases: 470. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 470 | 0.3188 | 0.3271 |
| rnafold | ok | 470 | 0.2224 | 0.2206 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 262 | -0.0318 | 0.1743 |
| seed_p | 262 | -0.0605 | -0.0503 |
| seed_p_vs_seed_pars | 158 | -0.2052 | -0.2569 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
