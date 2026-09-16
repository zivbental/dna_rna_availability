# YDR172W
Status: ok. Length: 2273 nt. Measured usable bases: 1639. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1639 | 0.3305 | 0.3174 |
| rnafold | ok | 1639 | 0.2460 | 0.2302 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1129 | -0.0859 | -0.0398 |
| seed_p | 1129 | -0.2058 | -0.1379 |
| seed_p_vs_seed_pars | 937 | -0.3189 | -0.2814 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
