# YOR185C
Status: ok. Length: 1044 nt. Measured usable bases: 347. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 347 | 0.3167 | 0.2921 |
| rnafold | ok | 347 | 0.2553 | 0.2239 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 46 | -0.4005 | -0.6222 |
| seed_p | 46 | -0.6693 | -0.5822 |
| seed_p_vs_seed_pars | 34 | -0.6993 | -0.9185 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
