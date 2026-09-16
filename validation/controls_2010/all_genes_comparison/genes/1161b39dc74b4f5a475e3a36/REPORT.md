# YLR310C
Status: ok. Length: 4967 nt. Measured usable bases: 1713. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1713 | 0.3137 | 0.3094 |
| rnafold | ok | 1713 | 0.2633 | 0.2695 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 259 | 0.0259 | -0.1345 |
| seed_p | 259 | -0.0129 | 0.0490 |
| seed_p_vs_seed_pars | 205 | -0.2675 | 0.0325 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
