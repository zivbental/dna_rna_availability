# YDL092W
Status: ok. Length: 588 nt. Measured usable bases: 356. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 356 | 0.3179 | 0.3463 |
| rnafold | ok | 356 | 0.2283 | 0.2420 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 182 | -0.1667 | -0.1649 |
| seed_p | 182 | -0.0911 | -0.0308 |
| seed_p_vs_seed_pars | 134 | -0.1698 | -0.0533 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
