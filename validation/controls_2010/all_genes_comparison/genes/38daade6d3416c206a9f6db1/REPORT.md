# YMR237W
Status: ok. Length: 2392 nt. Measured usable bases: 1251. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1251 | 0.3355 | 0.3114 |
| rnafold | ok | 1251 | 0.3157 | 0.2912 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 211 | -0.1902 | -0.3539 |
| seed_p | 211 | -0.0496 | -0.1015 |
| seed_p_vs_seed_pars | 158 | -0.3334 | -0.3481 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
