# YLR243W
Status: ok. Length: 974 nt. Measured usable bases: 482. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 482 | 0.3191 | 0.3030 |
| rnafold | ok | 482 | 0.3042 | 0.2864 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 124 | -0.0047 | -0.0732 |
| seed_p | 124 | 0.2023 | 0.2233 |
| seed_p_vs_seed_pars | 86 | -0.4577 | -0.3719 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
