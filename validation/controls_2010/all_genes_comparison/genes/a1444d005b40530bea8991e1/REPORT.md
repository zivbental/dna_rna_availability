# YGR095C
Status: ok. Length: 746 nt. Measured usable bases: 383. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 383 | 0.3308 | 0.3384 |
| rnafold | ok | 383 | 0.2603 | 0.2728 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 64 | -0.6109 | -0.7577 |
| seed_p | 64 | -0.3066 | -0.5617 |
| seed_p_vs_seed_pars | 55 | -0.3145 | -0.4845 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
