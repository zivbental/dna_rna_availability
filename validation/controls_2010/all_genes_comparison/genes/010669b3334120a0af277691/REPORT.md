# YKR052C
Status: ok. Length: 1313 nt. Measured usable bases: 450. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 450 | 0.4417 | 0.4391 |
| rnafold | ok | 450 | 0.3601 | 0.3591 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 47 | -0.6332 | -0.7160 |
| seed_p | 47 | -0.8663 | -0.7786 |
| seed_p_vs_seed_pars | 23 | -0.5481 | -0.5719 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
