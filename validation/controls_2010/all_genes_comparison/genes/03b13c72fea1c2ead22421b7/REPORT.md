# YML018C
Status: ok. Length: 1436 nt. Measured usable bases: 900. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 900 | 0.2128 | 0.1929 |
| rnafold | ok | 900 | 0.2092 | 0.1976 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 529 | 0.1429 | -0.0348 |
| seed_p | 529 | -0.1500 | -0.1819 |
| seed_p_vs_seed_pars | 404 | -0.1582 | -0.2018 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
