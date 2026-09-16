# YNL280C
Status: ok. Length: 1474 nt. Measured usable bases: 1045. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1045 | 0.2521 | 0.2530 |
| rnafold | ok | 1045 | 0.2159 | 0.2294 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 726 | 0.0832 | 0.0162 |
| seed_p | 726 | -0.1743 | -0.1952 |
| seed_p_vs_seed_pars | 608 | -0.2425 | -0.2015 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
