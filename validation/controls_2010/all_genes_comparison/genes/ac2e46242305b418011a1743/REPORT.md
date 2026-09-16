# YPL063W
Status: ok. Length: 1619 nt. Measured usable bases: 864. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 864 | 0.3183 | 0.3218 |
| rnafold | ok | 864 | 0.2515 | 0.2652 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 170 | -0.1985 | -0.3414 |
| seed_p | 170 | -0.3941 | -0.4423 |
| seed_p_vs_seed_pars | 134 | -0.3899 | -0.4352 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
