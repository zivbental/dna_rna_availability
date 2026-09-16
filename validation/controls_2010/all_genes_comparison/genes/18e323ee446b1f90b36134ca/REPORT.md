# YPL183W-A
Status: ok. Length: 473 nt. Measured usable bases: 274. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 274 | 0.2516 | 0.2492 |
| rnafold | ok | 274 | 0.2845 | 0.2906 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 177 | 0.0938 | 0.1595 |
| seed_p | 177 | 0.1359 | 0.1746 |
| seed_p_vs_seed_pars | 140 | -0.0473 | -0.0570 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
