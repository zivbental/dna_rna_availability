# YDL160C-A
Status: ok. Length: 433 nt. Measured usable bases: 198. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 198 | 0.3837 | 0.3936 |
| rnafold | ok | 198 | 0.4127 | 0.4329 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 31 | 0.7198 | 0.6020 |
| seed_p | 31 | 0.1201 | 0.0819 |
| seed_p_vs_seed_pars | 23 | 0.4617 | 0.6145 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
