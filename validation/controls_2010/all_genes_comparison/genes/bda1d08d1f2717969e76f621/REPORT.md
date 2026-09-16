# YGR116W
Status: ok. Length: 4513 nt. Measured usable bases: 1778. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1778 | 0.3562 | 0.3513 |
| rnafold | ok | 1778 | 0.2974 | 0.3002 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 157 | -0.0835 | -0.3098 |
| seed_p | 157 | -0.1326 | -0.1506 |
| seed_p_vs_seed_pars | 110 | -0.2024 | -0.0807 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
