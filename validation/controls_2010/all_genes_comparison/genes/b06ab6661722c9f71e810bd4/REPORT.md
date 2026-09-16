# YOL052C-A
Status: ok. Length: 464 nt. Measured usable bases: 162. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 162 | 0.1923 | 0.1600 |
| rnafold | ok | 162 | 0.1094 | 0.0807 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 47 | -0.1257 | -0.5299 |
| seed_p | 47 | 0.1207 | 0.0769 |
| seed_p_vs_seed_pars | 44 | 0.0738 | 0.0623 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
