# YDR329C
Status: ok. Length: 1430 nt. Measured usable bases: 675. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 675 | 0.3920 | 0.3969 |
| rnafold | ok | 675 | 0.2964 | 0.3118 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 114 | -0.2485 | -0.0843 |
| seed_p | 114 | 0.0375 | -0.0172 |
| seed_p_vs_seed_pars | 70 | 0.3282 | 0.3648 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
