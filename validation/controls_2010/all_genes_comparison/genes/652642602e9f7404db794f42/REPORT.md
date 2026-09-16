# YHR020W
Status: ok. Length: 2261 nt. Measured usable bases: 1906. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1906 | 0.3153 | 0.3030 |
| rnafold | ok | 1906 | 0.2487 | 0.2526 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1817 | 0.0345 | -0.0147 |
| seed_p | 1817 | -0.1636 | -0.1321 |
| seed_p_vs_seed_pars | 1537 | -0.2850 | -0.2141 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
