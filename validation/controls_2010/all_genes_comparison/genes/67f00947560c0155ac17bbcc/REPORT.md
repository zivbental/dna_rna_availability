# YMR212C
Status: ok. Length: 2569 nt. Measured usable bases: 1459. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1459 | 0.3024 | 0.2951 |
| rnafold | ok | 1459 | 0.2348 | 0.2324 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 411 | -0.0845 | -0.2443 |
| seed_p | 411 | -0.1699 | -0.2645 |
| seed_p_vs_seed_pars | 299 | -0.3564 | -0.3959 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
