# YHR026W
Status: ok. Length: 893 nt. Measured usable bases: 679. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 679 | 0.3329 | 0.3316 |
| rnafold | ok | 679 | 0.3178 | 0.3278 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 621 | -0.0012 | 0.0622 |
| seed_p | 621 | -0.2513 | -0.1096 |
| seed_p_vs_seed_pars | 529 | -0.3151 | -0.2435 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
