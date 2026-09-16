# YNL192W
Status: ok. Length: 3617 nt. Measured usable bases: 1695. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1695 | 0.2574 | 0.2408 |
| rnafold | ok | 1695 | 0.2107 | 0.1976 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 258 | -0.2285 | -0.3615 |
| seed_p | 258 | -0.1797 | -0.1376 |
| seed_p_vs_seed_pars | 162 | -0.3918 | -0.3427 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
