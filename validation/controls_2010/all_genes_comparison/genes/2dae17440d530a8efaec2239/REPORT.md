# YGR082W
Status: ok. Length: 749 nt. Measured usable bases: 539. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 539 | 0.2970 | 0.2928 |
| rnafold | ok | 539 | 0.2751 | 0.2743 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 393 | 0.0094 | -0.1152 |
| seed_p | 393 | 0.1453 | 0.0606 |
| seed_p_vs_seed_pars | 343 | 0.0198 | -0.0896 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
