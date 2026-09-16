# YPL059W
Status: ok. Length: 652 nt. Measured usable bases: 482. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 482 | 0.3732 | 0.3749 |
| rnafold | ok | 482 | 0.3346 | 0.3464 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 336 | -0.2920 | -0.3903 |
| seed_p | 336 | -0.2466 | -0.3525 |
| seed_p_vs_seed_pars | 294 | -0.2630 | -0.2988 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
