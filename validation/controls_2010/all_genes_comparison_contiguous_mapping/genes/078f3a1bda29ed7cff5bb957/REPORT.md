# YBL024W
Status: ok. Length: 2255 nt. Measured usable bases: 1174.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1174 | 0.2910 | 0.2528 |
| rnafold | ok | 1174 | 0.2627 | 0.2334 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 308 | 0.0801 | 0.2670 |
| seed_p | 308 | 0.2281 | 0.2284 |
| seed_p_vs_seed_pars | 194 | 0.0460 | 0.0064 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
