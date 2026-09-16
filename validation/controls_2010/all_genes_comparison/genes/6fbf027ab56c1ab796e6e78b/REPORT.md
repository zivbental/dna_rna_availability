# YOR335C
Status: ok. Length: 3085 nt. Measured usable bases: 2357. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2357 | 0.3236 | 0.3184 |
| rnafold | ok | 2357 | 0.2708 | 0.2647 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1692 | -0.1282 | -0.1792 |
| seed_p | 1692 | -0.2372 | -0.2207 |
| seed_p_vs_seed_pars | 1380 | -0.2707 | -0.2443 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
