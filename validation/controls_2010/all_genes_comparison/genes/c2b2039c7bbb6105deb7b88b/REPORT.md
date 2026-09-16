# YDR418W
Status: ok. Length: 600 nt. Measured usable bases: 384. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 384 | 0.4016 | 0.3934 |
| rnafold | ok | 384 | 0.3549 | 0.3647 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 293 | -0.6191 | -0.4371 |
| seed_p | 293 | -0.6339 | -0.5181 |
| seed_p_vs_seed_pars | 282 | -0.4468 | -0.4490 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
