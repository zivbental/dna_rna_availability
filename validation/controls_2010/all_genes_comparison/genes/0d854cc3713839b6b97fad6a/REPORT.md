# YOR355W
Status: ok. Length: 1851 nt. Measured usable bases: 1080. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1080 | 0.3080 | 0.2939 |
| rnafold | ok | 1080 | 0.2523 | 0.2564 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 446 | -0.1334 | -0.2217 |
| seed_p | 446 | -0.1621 | -0.1756 |
| seed_p_vs_seed_pars | 321 | -0.3831 | -0.3717 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
