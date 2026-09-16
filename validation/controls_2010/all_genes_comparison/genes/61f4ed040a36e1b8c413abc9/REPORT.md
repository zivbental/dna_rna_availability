# YNL002C
Status: ok. Length: 1046 nt. Measured usable bases: 507. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 507 | 0.2524 | 0.2585 |
| rnafold | ok | 507 | 0.1893 | 0.1935 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 107 | -0.2190 | -0.1374 |
| seed_p | 107 | -0.1387 | -0.2338 |
| seed_p_vs_seed_pars | 67 | -0.4676 | -0.4890 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
