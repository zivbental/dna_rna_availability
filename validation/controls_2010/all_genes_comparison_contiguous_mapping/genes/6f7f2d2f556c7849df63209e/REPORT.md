# YBL028C
Status: ok. Length: 549 nt. Measured usable bases: 274.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 274 | 0.3758 | 0.3671 |
| rnafold | ok | 274 | 0.3869 | 0.3990 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 58 | -0.1672 | -0.4280 |
| seed_p | 58 | -0.1346 | -0.2149 |
| seed_p_vs_seed_pars | 47 | -0.0166 | -0.4615 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
