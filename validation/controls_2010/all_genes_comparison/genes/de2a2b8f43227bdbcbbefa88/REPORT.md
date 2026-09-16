# YNL268W
Status: ok. Length: 2100 nt. Measured usable bases: 1390. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1390 | 0.3335 | 0.3209 |
| rnafold | ok | 1390 | 0.2548 | 0.2446 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 658 | -0.2425 | -0.2654 |
| seed_p | 658 | -0.3708 | -0.3598 |
| seed_p_vs_seed_pars | 472 | -0.4353 | -0.4689 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
