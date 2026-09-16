# YOR220W
Status: ok. Length: 997 nt. Measured usable bases: 371. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 371 | 0.2778 | 0.2853 |
| rnafold | ok | 371 | 0.2900 | 0.2929 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 25 | 0.4647 | 0.3920 |
| seed_p | 25 | 0.7441 | 0.7646 |
| seed_p_vs_seed_pars | 22 | 0.6984 | 0.5561 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
