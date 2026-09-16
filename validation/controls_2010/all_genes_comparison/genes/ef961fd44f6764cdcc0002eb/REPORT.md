# YDL230W
Status: ok. Length: 1122 nt. Measured usable bases: 474. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 474 | 0.3351 | 0.3195 |
| rnafold | ok | 474 | 0.1690 | 0.1426 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 65 | -0.5003 | -0.1920 |
| seed_p | 65 | -0.1733 | -0.1299 |
| seed_p_vs_seed_pars | 60 | -0.1880 | -0.2540 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
