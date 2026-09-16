# YEL044W
Status: ok. Length: 655 nt. Measured usable bases: 345. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 345 | 0.4518 | 0.4336 |
| rnafold | ok | 345 | 0.3926 | 0.3724 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 165 | -0.4835 | -0.4279 |
| seed_p | 165 | -0.5420 | -0.4884 |
| seed_p_vs_seed_pars | 127 | -0.6521 | -0.5146 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
