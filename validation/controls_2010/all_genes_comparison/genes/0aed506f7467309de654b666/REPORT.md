# YML078W
Status: ok. Length: 699 nt. Measured usable bases: 547. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 547 | 0.2744 | 0.2674 |
| rnafold | ok | 547 | 0.2495 | 0.2514 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 484 | 0.0919 | 0.1753 |
| seed_p | 484 | -0.1049 | 0.0624 |
| seed_p_vs_seed_pars | 379 | -0.0121 | 0.0661 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
