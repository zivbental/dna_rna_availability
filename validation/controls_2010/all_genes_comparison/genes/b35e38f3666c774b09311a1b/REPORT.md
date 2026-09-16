# YML117W
Status: ok. Length: 3405 nt. Measured usable bases: 1343. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1343 | 0.2772 | 0.2752 |
| rnafold | ok | 1343 | 0.2250 | 0.2432 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 85 | -0.0422 | -0.1826 |
| seed_p | 85 | 0.1494 | 0.1770 |
| seed_p_vs_seed_pars | 57 | -0.1224 | -0.0241 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
