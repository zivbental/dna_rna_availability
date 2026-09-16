# YFR049W
Status: ok. Length: 652 nt. Measured usable bases: 242. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 242 | 0.4176 | 0.4282 |
| rnafold | ok | 242 | 0.3658 | 0.3832 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 44 | -0.6124 | -0.4722 |
| seed_p | 44 | -0.4689 | -0.4955 |
| seed_p_vs_seed_pars | 37 | -0.0641 | 0.0412 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
