# YMR008C
Status: ok. Length: 2447 nt. Measured usable bases: 1032. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1032 | 0.3318 | 0.3286 |
| rnafold | ok | 1032 | 0.2650 | 0.2739 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 61 | -0.5417 | -0.3941 |
| seed_p | 61 | -0.5161 | -0.2140 |
| seed_p_vs_seed_pars | 49 | -0.5339 | -0.1342 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
