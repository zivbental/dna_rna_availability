# YNL216W
Status: ok. Length: 2692 nt. Measured usable bases: 1528. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1528 | 0.2941 | 0.2868 |
| rnafold | ok | 1528 | 0.2640 | 0.2679 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 407 | 0.1710 | 0.1588 |
| seed_p | 407 | -0.0295 | -0.0486 |
| seed_p_vs_seed_pars | 317 | -0.1066 | -0.0167 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
