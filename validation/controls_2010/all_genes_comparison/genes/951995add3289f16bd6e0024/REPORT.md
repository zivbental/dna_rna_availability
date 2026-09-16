# YER020W
Status: ok. Length: 1632 nt. Measured usable bases: 643. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 643 | 0.3066 | 0.3098 |
| rnafold | ok | 643 | 0.2698 | 0.2701 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 67 | 0.2137 | 0.1985 |
| seed_p | 67 | -0.0891 | 0.0185 |
| seed_p_vs_seed_pars | 54 | -0.2139 | 0.0736 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
