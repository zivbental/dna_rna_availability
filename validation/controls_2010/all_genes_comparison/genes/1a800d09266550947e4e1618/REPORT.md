# YGR054W
Status: ok. Length: 2152 nt. Measured usable bases: 1477. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1477 | 0.2716 | 0.2644 |
| rnafold | ok | 1477 | 0.2713 | 0.2846 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 818 | -0.0377 | -0.1018 |
| seed_p | 818 | -0.1062 | -0.1428 |
| seed_p_vs_seed_pars | 672 | -0.1230 | -0.1497 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
