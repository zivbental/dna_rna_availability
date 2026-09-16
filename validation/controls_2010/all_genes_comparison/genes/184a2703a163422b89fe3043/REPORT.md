# YDL215C
Status: ok. Length: 3635 nt. Measured usable bases: 1263. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1263 | 0.3320 | 0.3050 |
| rnafold | ok | 1263 | 0.2740 | 0.2482 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 81 | -0.0217 | 0.0215 |
| seed_p | 81 | -0.2663 | -0.1107 |
| seed_p_vs_seed_pars | 48 | -0.3935 | -0.2926 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
