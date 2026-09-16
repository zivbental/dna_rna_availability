# RDN25-1
Status: ok. Length: 3396 nt. Measured usable bases: 3348. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 3348 | 0.4711 | 0.4563 |
| rnafold | ok | 3348 | 0.4030 | 0.4136 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 3339 | -0.0047 | -0.1925 |
| seed_p | 3339 | -0.1808 | -0.2096 |
| seed_p_vs_seed_pars | 3327 | -0.3458 | -0.3124 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
