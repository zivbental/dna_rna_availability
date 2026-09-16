# YOR071C
Status: ok. Length: 1797 nt. Measured usable bases: 741. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 741 | 0.2904 | 0.2632 |
| rnafold | ok | 741 | 0.2560 | 0.2497 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 62 | 0.1248 | 0.3987 |
| seed_p | 62 | 0.2063 | 0.0965 |
| seed_p_vs_seed_pars | 34 | -0.4072 | -0.5025 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
