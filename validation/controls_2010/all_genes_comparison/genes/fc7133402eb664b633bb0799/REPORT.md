# YOL002C
Status: ok. Length: 1050 nt. Measured usable bases: 631. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 631 | 0.2615 | 0.2583 |
| rnafold | ok | 631 | 0.2040 | 0.2033 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 250 | -0.1923 | 0.0366 |
| seed_p | 250 | -0.0044 | 0.0605 |
| seed_p_vs_seed_pars | 201 | -0.1405 | 0.1323 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
