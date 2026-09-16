# LSR1
Status: ok. Length: 1175 nt. Measured usable bases: 383.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 383 | 0.4158 | 0.4211 |
| rnafold | ok | 383 | 0.2136 | 0.1423 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 59 | 0.3404 | -0.0215 |
| seed_p | 59 | -0.0164 | -0.0261 |
| seed_p_vs_seed_pars | 43 | -0.1458 | 0.1007 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
