# YIL074C
Status: ok. Length: 1551 nt. Measured usable bases: 1043. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1043 | 0.3132 | 0.3016 |
| rnafold | ok | 1043 | 0.2515 | 0.2496 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 548 | 0.0913 | -0.0631 |
| seed_p | 548 | -0.3042 | -0.1134 |
| seed_p_vs_seed_pars | 342 | -0.4223 | -0.2532 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
