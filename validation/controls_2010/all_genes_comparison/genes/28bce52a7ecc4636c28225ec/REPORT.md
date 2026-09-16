# YGL063W
Status: ok. Length: 1113 nt. Measured usable bases: 487. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 487 | 0.2869 | 0.2736 |
| rnafold | ok | 487 | 0.1952 | 0.2000 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 46 | -0.5065 | -0.4017 |
| seed_p | 46 | 0.3736 | 0.3363 |
| seed_p_vs_seed_pars | 34 | -0.5896 | -0.5977 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
