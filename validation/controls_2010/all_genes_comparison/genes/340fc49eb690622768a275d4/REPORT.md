# YDR007W
Status: ok. Length: 902 nt. Measured usable bases: 533. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 533 | 0.2864 | 0.2636 |
| rnafold | ok | 533 | 0.2499 | 0.2463 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 179 | -0.0806 | 0.0263 |
| seed_p | 179 | -0.2814 | -0.0301 |
| seed_p_vs_seed_pars | 140 | -0.6130 | -0.3212 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
