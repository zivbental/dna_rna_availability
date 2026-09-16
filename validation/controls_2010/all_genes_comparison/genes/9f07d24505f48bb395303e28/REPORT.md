# YOR261C
Status: ok. Length: 1176 nt. Measured usable bases: 699. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 699 | 0.3737 | 0.3691 |
| rnafold | ok | 699 | 0.3351 | 0.3336 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 291 | -0.1153 | -0.0339 |
| seed_p | 291 | -0.1696 | -0.2527 |
| seed_p_vs_seed_pars | 256 | -0.1892 | -0.2744 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
