# YGR061C
Status: ok. Length: 4475 nt. Measured usable bases: 2943. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2943 | 0.3410 | 0.3211 |
| rnafold | ok | 2943 | 0.2640 | 0.2518 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1660 | -0.0250 | -0.1441 |
| seed_p | 1660 | -0.2645 | -0.2409 |
| seed_p_vs_seed_pars | 1308 | -0.3017 | -0.2891 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
