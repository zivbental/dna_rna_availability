# YKL194C
Status: ok. Length: 1796 nt. Measured usable bases: 545. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 545 | 0.3629 | 0.3472 |
| rnafold | ok | 545 | 0.2440 | 0.2313 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 35 | 0.1824 | 0.6424 |
| seed_p | 35 | 0.8539 | 0.8357 |
| seed_p_vs_seed_pars | 29 | 0.6740 | 0.6741 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
