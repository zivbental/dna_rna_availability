# YGR204W
Status: ok. Length: 2962 nt. Measured usable bases: 2414. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2414 | 0.2993 | 0.2837 |
| rnafold | ok | 2414 | 0.2509 | 0.2466 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 2019 | -0.1234 | -0.1330 |
| seed_p | 2019 | -0.2725 | -0.2439 |
| seed_p_vs_seed_pars | 1756 | -0.4141 | -0.3430 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
