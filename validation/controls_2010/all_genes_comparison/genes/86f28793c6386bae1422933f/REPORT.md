# YLR172C
Status: ok. Length: 975 nt. Measured usable bases: 714. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 714 | 0.3410 | 0.3427 |
| rnafold | ok | 714 | 0.3244 | 0.3347 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 485 | -0.0856 | -0.0539 |
| seed_p | 485 | -0.1169 | -0.1194 |
| seed_p_vs_seed_pars | 413 | -0.2457 | -0.2323 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
