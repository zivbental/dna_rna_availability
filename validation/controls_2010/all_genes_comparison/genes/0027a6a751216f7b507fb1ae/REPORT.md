# YFL018C
Status: ok. Length: 1652 nt. Measured usable bases: 1168. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1168 | 0.3725 | 0.3531 |
| rnafold | ok | 1168 | 0.3244 | 0.3152 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 703 | -0.0085 | -0.1553 |
| seed_p | 703 | 0.0342 | -0.0576 |
| seed_p_vs_seed_pars | 600 | -0.0401 | -0.1616 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
