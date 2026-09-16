# YPL126W
Status: ok. Length: 2824 nt. Measured usable bases: 1648. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1648 | 0.3066 | 0.2958 |
| rnafold | ok | 1648 | 0.2336 | 0.2228 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 528 | 0.0552 | 0.0987 |
| seed_p | 528 | -0.3718 | -0.3181 |
| seed_p_vs_seed_pars | 429 | -0.4241 | -0.4743 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
