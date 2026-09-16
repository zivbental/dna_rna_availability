# YLR065C
Status: ok. Length: 654 nt. Measured usable bases: 402. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 402 | 0.3072 | 0.3118 |
| rnafold | ok | 402 | 0.2977 | 0.2882 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 218 | -0.1347 | -0.1247 |
| seed_p | 218 | -0.4546 | -0.3251 |
| seed_p_vs_seed_pars | 158 | -0.4331 | -0.3263 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
