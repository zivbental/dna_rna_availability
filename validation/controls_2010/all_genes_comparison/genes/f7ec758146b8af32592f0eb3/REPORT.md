# YIR022W
Status: ok. Length: 606 nt. Measured usable bases: 504. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 504 | 0.3496 | 0.3432 |
| rnafold | ok | 504 | 0.2728 | 0.2653 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 431 | 0.0141 | -0.2269 |
| seed_p | 431 | 0.0011 | -0.0740 |
| seed_p_vs_seed_pars | 359 | -0.1880 | -0.2629 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
