# YOR286W
Status: ok. Length: 527 nt. Measured usable bases: 386. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 386 | 0.4360 | 0.4258 |
| rnafold | ok | 386 | 0.4027 | 0.3930 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 293 | -0.0724 | -0.4395 |
| seed_p | 293 | -0.4041 | -0.4241 |
| seed_p_vs_seed_pars | 214 | -0.6292 | -0.5684 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
