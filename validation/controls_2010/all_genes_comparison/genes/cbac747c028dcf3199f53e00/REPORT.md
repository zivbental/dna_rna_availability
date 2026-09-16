# YPL047W
Status: ok. Length: 720 nt. Measured usable bases: 490. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 490 | 0.1939 | 0.2103 |
| rnafold | ok | 490 | 0.1946 | 0.2129 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 289 | -0.1878 | -0.2022 |
| seed_p | 289 | -0.2569 | -0.3334 |
| seed_p_vs_seed_pars | 206 | -0.0028 | -0.1935 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
