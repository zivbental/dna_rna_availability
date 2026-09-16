# YJR067C
Status: ok. Length: 525 nt. Measured usable bases: 212. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 212 | 0.2704 | 0.2715 |
| rnafold | ok | 212 | 0.1378 | 0.1540 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 26 | -0.1048 | -0.3259 |
| seed_p | 26 | -0.3881 | -0.1076 |
| seed_p_vs_seed_pars | 15 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
