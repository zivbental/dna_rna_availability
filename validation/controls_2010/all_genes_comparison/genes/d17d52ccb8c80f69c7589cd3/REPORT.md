# YMR290C
Status: ok. Length: 1723 nt. Measured usable bases: 1021. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1021 | 0.2642 | 0.2417 |
| rnafold | ok | 1021 | 0.1969 | 0.2012 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 403 | -0.0448 | -0.0497 |
| seed_p | 403 | -0.1344 | -0.3048 |
| seed_p_vs_seed_pars | 284 | -0.2799 | -0.4277 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
