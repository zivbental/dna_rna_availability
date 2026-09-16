# YMR011W
Status: ok. Length: 1786 nt. Measured usable bases: 1325. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1325 | 0.2906 | 0.2813 |
| rnafold | ok | 1325 | 0.1805 | 0.1821 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 960 | -0.1166 | -0.1970 |
| seed_p | 960 | -0.2950 | -0.2600 |
| seed_p_vs_seed_pars | 784 | -0.2577 | -0.2780 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
