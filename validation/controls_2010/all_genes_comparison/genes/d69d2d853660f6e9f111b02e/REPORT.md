# YML022W
Status: ok. Length: 813 nt. Measured usable bases: 658. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 658 | 0.3471 | 0.3368 |
| rnafold | ok | 658 | 0.2488 | 0.2395 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 554 | -0.1202 | -0.4466 |
| seed_p | 554 | -0.2373 | -0.2813 |
| seed_p_vs_seed_pars | 507 | -0.3639 | -0.3417 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
