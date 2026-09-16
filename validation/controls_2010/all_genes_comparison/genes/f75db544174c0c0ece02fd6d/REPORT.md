# YOR342C
Status: ok. Length: 1277 nt. Measured usable bases: 533. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 533 | 0.2567 | 0.2343 |
| rnafold | ok | 533 | 0.2250 | 0.2109 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 41 | -0.2092 | 0.0483 |
| seed_p | 41 | -0.5134 | -0.4558 |
| seed_p_vs_seed_pars | 22 | -0.1782 | 0.2832 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
