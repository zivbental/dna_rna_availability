# YFR051C
Status: ok. Length: 1734 nt. Measured usable bases: 1321. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1321 | 0.3116 | 0.2956 |
| rnafold | ok | 1321 | 0.2678 | 0.2577 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 992 | -0.0296 | -0.0546 |
| seed_p | 992 | -0.3128 | -0.2769 |
| seed_p_vs_seed_pars | 816 | -0.4132 | -0.4172 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
