# YNL281W
Status: ok. Length: 654 nt. Measured usable bases: 468. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 468 | 0.4728 | 0.4442 |
| rnafold | ok | 468 | 0.4357 | 0.4402 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 395 | -0.1207 | -0.2455 |
| seed_p | 395 | -0.2785 | -0.2604 |
| seed_p_vs_seed_pars | 320 | -0.4194 | -0.4440 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
