# YLR237W
Status: ok. Length: 1797 nt. Measured usable bases: 744. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 744 | 0.2992 | 0.2882 |
| rnafold | ok | 744 | 0.2294 | 0.2084 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 62 | -0.1208 | -0.4188 |
| seed_p | 62 | -0.0687 | -0.2152 |
| seed_p_vs_seed_pars | 42 | -0.4238 | -0.5188 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
