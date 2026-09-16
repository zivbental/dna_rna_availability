# YNL036W
Status: ok. Length: 829 nt. Measured usable bases: 471. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 471 | 0.2556 | 0.2568 |
| rnafold | ok | 471 | 0.2336 | 0.2262 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 119 | 0.3784 | 0.4776 |
| seed_p | 119 | 0.0899 | 0.2199 |
| seed_p_vs_seed_pars | 100 | -0.0776 | -0.0559 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
