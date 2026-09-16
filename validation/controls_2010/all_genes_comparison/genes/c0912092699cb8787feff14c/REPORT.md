# YDL020C
Status: ok. Length: 1958 nt. Measured usable bases: 863. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 863 | 0.3388 | 0.3380 |
| rnafold | ok | 863 | 0.2768 | 0.2959 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 108 | -0.1742 | -0.3336 |
| seed_p | 108 | -0.4799 | -0.4368 |
| seed_p_vs_seed_pars | 94 | -0.6228 | -0.5799 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
