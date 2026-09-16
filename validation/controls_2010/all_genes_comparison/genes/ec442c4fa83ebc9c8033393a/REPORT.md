# YBR038W
Status: ok. Length: 3158 nt. Measured usable bases: 1424. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1424 | 0.2757 | 0.2637 |
| rnafold | ok | 1424 | 0.1753 | 0.1691 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 213 | 0.0498 | -0.2410 |
| seed_p | 213 | 0.1517 | 0.0274 |
| seed_p_vs_seed_pars | 175 | -0.0075 | -0.0295 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
