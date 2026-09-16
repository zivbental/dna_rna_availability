# YLR009W
Status: ok. Length: 912 nt. Measured usable bases: 458. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 458 | 0.3423 | 0.3357 |
| rnafold | ok | 458 | 0.3631 | 0.3391 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 108 | 0.2528 | 0.0322 |
| seed_p | 108 | -0.4301 | -0.5099 |
| seed_p_vs_seed_pars | 68 | -0.3847 | -0.4201 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
