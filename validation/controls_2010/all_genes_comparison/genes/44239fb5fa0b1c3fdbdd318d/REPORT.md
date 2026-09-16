# YKL165C
Status: ok. Length: 2858 nt. Measured usable bases: 1575. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1575 | 0.2583 | 0.2451 |
| rnafold | ok | 1575 | 0.2183 | 0.2134 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 375 | -0.1569 | -0.0577 |
| seed_p | 375 | -0.2821 | -0.2451 |
| seed_p_vs_seed_pars | 234 | -0.4486 | -0.3208 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
