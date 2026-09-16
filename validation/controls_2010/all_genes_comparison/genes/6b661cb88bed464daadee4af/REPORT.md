# YIL162W
Status: ok. Length: 1834 nt. Measured usable bases: 977. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 977 | 0.2967 | 0.2622 |
| rnafold | ok | 977 | 0.1695 | 0.1361 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 272 | -0.1815 | 0.0464 |
| seed_p | 272 | 0.0565 | 0.0638 |
| seed_p_vs_seed_pars | 195 | -0.1572 | -0.1797 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
