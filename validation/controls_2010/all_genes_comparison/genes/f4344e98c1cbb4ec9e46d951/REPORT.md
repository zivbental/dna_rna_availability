# YGR038W
Status: ok. Length: 956 nt. Measured usable bases: 588. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 588 | 0.2978 | 0.2899 |
| rnafold | ok | 588 | 0.2878 | 0.2833 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 297 | -0.0643 | -0.2233 |
| seed_p | 297 | -0.2176 | -0.2608 |
| seed_p_vs_seed_pars | 237 | -0.1677 | -0.1807 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
