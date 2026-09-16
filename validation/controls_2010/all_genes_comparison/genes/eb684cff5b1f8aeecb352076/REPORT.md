# YLR222C
Status: ok. Length: 2553 nt. Measured usable bases: 1136. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1136 | 0.3032 | 0.2948 |
| rnafold | ok | 1136 | 0.2271 | 0.2092 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 101 | 0.0558 | 0.1951 |
| seed_p | 101 | 0.0290 | -0.0670 |
| seed_p_vs_seed_pars | 71 | 0.0069 | -0.0511 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
