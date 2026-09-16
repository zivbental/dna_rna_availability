# YEL017W
Status: ok. Length: 1233 nt. Measured usable bases: 701. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 701 | 0.3410 | 0.3456 |
| rnafold | ok | 701 | 0.2758 | 0.2746 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 287 | -0.4251 | -0.0807 |
| seed_p | 287 | -0.2823 | -0.2006 |
| seed_p_vs_seed_pars | 241 | -0.1638 | -0.1572 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
