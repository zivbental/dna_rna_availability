# YAL053W
Status: ok. Length: 2514 nt. Measured usable bases: 1449.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1449 | 0.2657 | 0.2631 |
| rnafold | ok | 1449 | 0.2195 | 0.2163 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 586 | -0.0558 | -0.3077 |
| seed_p | 586 | -0.0635 | -0.1342 |
| seed_p_vs_seed_pars | 433 | -0.3534 | -0.4070 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
