# YOL012C
Status: ok. Length: 635 nt. Measured usable bases: 401. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 401 | 0.3034 | 0.2902 |
| rnafold | ok | 401 | 0.2989 | 0.2913 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 171 | -0.1342 | -0.3019 |
| seed_p | 171 | -0.2583 | -0.3498 |
| seed_p_vs_seed_pars | 129 | -0.2385 | -0.4521 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
