# YMR236W
Status: ok. Length: 607 nt. Measured usable bases: 450. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 450 | 0.3152 | 0.3122 |
| rnafold | ok | 450 | 0.2601 | 0.2618 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 338 | -0.1153 | -0.1048 |
| seed_p | 338 | -0.2140 | -0.2141 |
| seed_p_vs_seed_pars | 285 | -0.4074 | -0.4040 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
