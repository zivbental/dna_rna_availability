# YBR121C
Status: ok. Length: 2166 nt. Measured usable bases: 1708. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1708 | 0.3852 | 0.3508 |
| rnafold | ok | 1708 | 0.3098 | 0.2817 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1359 | -0.0754 | -0.2191 |
| seed_p | 1359 | -0.2134 | -0.2238 |
| seed_p_vs_seed_pars | 1148 | -0.3413 | -0.2992 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
