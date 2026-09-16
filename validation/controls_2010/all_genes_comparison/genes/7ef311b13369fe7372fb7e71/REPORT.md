# YGR201C
Status: ok. Length: 792 nt. Measured usable bases: 369. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 369 | 0.3440 | 0.3498 |
| rnafold | ok | 369 | 0.2602 | 0.3100 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 81 | -0.5336 | -0.5156 |
| seed_p | 81 | -0.5701 | -0.4307 |
| seed_p_vs_seed_pars | 42 | -0.5036 | -0.5111 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
