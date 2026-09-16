# TLC1
Status: ok. Length: 1301 nt. Measured usable bases: 734.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 734 | 0.2670 | 0.2557 |
| rnafold | ok | 734 | 0.1576 | 0.1946 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 361 | -0.0413 | -0.1419 |
| seed_p | 361 | -0.1254 | -0.1621 |
| seed_p_vs_seed_pars | 300 | -0.1401 | -0.2547 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
