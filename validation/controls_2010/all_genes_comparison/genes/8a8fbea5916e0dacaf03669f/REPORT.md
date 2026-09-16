# YER072W
Status: ok. Length: 576 nt. Measured usable bases: 514. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 514 | 0.1949 | 0.1878 |
| rnafold | ok | 514 | 0.1643 | 0.1571 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 499 | 0.0547 | 0.1169 |
| seed_p | 499 | 0.1110 | 0.1446 |
| seed_p_vs_seed_pars | 451 | -0.0832 | -0.1048 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
