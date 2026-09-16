# YMR267W
Status: ok. Length: 1192 nt. Measured usable bases: 475. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 475 | 0.2633 | 0.2498 |
| rnafold | ok | 475 | 0.2080 | 0.2181 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 55 | 0.0410 | -0.1537 |
| seed_p | 55 | -0.2632 | -0.3375 |
| seed_p_vs_seed_pars | 47 | -0.6232 | -0.6557 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
