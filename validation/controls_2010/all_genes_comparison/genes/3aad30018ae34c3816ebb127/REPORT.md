# YJR073C
Status: ok. Length: 711 nt. Measured usable bases: 533. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 533 | 0.2780 | 0.2478 |
| rnafold | ok | 533 | 0.2473 | 0.2020 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 357 | -0.0908 | -0.0374 |
| seed_p | 357 | 0.0510 | 0.0075 |
| seed_p_vs_seed_pars | 304 | -0.0270 | -0.0982 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
