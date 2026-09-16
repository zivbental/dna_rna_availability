# YKL113C
Status: ok. Length: 1403 nt. Measured usable bases: 461. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 461 | 0.3839 | 0.4019 |
| rnafold | ok | 461 | 0.3761 | 0.3961 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 32 | -0.3294 | -0.2054 |
| seed_p | 32 | -0.2106 | 0.2053 |
| seed_p_vs_seed_pars | 26 | -0.3661 | -0.1805 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
