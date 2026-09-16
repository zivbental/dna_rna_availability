# YOR217W
Status: ok. Length: 2889 nt. Measured usable bases: 1231. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1231 | 0.2647 | 0.2564 |
| rnafold | ok | 1231 | 0.2718 | 0.2661 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 262 | 0.1697 | 0.2689 |
| seed_p | 262 | 0.0783 | 0.1180 |
| seed_p_vs_seed_pars | 199 | 0.0490 | 0.0777 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
