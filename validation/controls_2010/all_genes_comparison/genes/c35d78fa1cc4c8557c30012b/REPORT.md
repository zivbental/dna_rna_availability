# YER102W
Status: ok. Length: 1036 nt. Measured usable bases: 271. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 271 | 0.4445 | 0.4515 |
| rnafold | ok | 271 | 0.3079 | 0.3126 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 105 | -0.0914 | -0.3457 |
| seed_p | 105 | -0.0980 | -0.0204 |
| seed_p_vs_seed_pars | 99 | -0.4822 | -0.4827 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
