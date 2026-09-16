# YPL037C
Status: ok. Length: 535 nt. Measured usable bases: 499. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 499 | 0.3381 | 0.3174 |
| rnafold | ok | 499 | 0.2819 | 0.2635 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 488 | 0.0617 | -0.0067 |
| seed_p | 488 | 0.1083 | 0.0813 |
| seed_p_vs_seed_pars | 483 | -0.1463 | -0.0969 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
