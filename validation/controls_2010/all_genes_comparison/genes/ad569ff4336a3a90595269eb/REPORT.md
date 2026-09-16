# YFL038C
Status: ok. Length: 768 nt. Measured usable bases: 623. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 623 | 0.2826 | 0.2766 |
| rnafold | ok | 623 | 0.2472 | 0.2804 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 516 | -0.2120 | 0.1620 |
| seed_p | 516 | 0.0570 | 0.1645 |
| seed_p_vs_seed_pars | 444 | -0.1321 | -0.0379 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
