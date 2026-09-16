# YOR285W
Status: ok. Length: 502 nt. Measured usable bases: 444. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 444 | 0.2426 | 0.2295 |
| rnafold | ok | 444 | 0.2350 | 0.2491 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 419 | -0.0278 | -0.0539 |
| seed_p | 419 | -0.1656 | -0.1067 |
| seed_p_vs_seed_pars | 392 | -0.2962 | -0.2926 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
