# YKR081C
Status: ok. Length: 1139 nt. Measured usable bases: 531. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 531 | 0.2809 | 0.2891 |
| rnafold | ok | 531 | 0.2972 | 0.2997 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 118 | 0.0693 | 0.0895 |
| seed_p | 118 | -0.4565 | -0.1715 |
| seed_p_vs_seed_pars | 53 | -0.5038 | -0.7295 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
