# YNL327W
Status: ok. Length: 3278 nt. Measured usable bases: 2377. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2377 | 0.2592 | 0.2539 |
| rnafold | ok | 2377 | 0.2261 | 0.2204 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1700 | -0.1254 | -0.1548 |
| seed_p | 1700 | -0.2727 | -0.2891 |
| seed_p_vs_seed_pars | 1318 | -0.3014 | -0.3353 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
