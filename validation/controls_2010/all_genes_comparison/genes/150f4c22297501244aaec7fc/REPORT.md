# YGR108W
Status: ok. Length: 1683 nt. Measured usable bases: 761. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 761 | 0.3295 | 0.3245 |
| rnafold | ok | 761 | 0.2515 | 0.2658 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 97 | -0.3290 | -0.6668 |
| seed_p | 97 | -0.4334 | -0.4635 |
| seed_p_vs_seed_pars | 69 | -0.3904 | -0.1195 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
