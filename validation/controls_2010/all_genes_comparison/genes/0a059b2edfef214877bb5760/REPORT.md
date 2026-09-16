# YHR072W-A
Status: ok. Length: 396 nt. Measured usable bases: 306. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 306 | 0.3789 | 0.3593 |
| rnafold | ok | 306 | 0.2857 | 0.2976 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 245 | -0.4455 | -0.4048 |
| seed_p | 245 | -0.3982 | -0.3911 |
| seed_p_vs_seed_pars | 228 | -0.3411 | -0.4030 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
