# YGL019W
Status: ok. Length: 1007 nt. Measured usable bases: 621. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 621 | 0.3539 | 0.3384 |
| rnafold | ok | 621 | 0.3592 | 0.3547 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 348 | -0.2660 | -0.2855 |
| seed_p | 348 | -0.3073 | -0.3018 |
| seed_p_vs_seed_pars | 284 | -0.2927 | -0.3761 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
