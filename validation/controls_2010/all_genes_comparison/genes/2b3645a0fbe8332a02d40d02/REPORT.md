# YGL020C
Status: ok. Length: 814 nt. Measured usable bases: 541. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 541 | 0.2177 | 0.1892 |
| rnafold | ok | 541 | 0.2058 | 0.1928 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 342 | -0.0876 | -0.2239 |
| seed_p | 342 | -0.2217 | -0.1804 |
| seed_p_vs_seed_pars | 235 | -0.3310 | -0.2547 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
