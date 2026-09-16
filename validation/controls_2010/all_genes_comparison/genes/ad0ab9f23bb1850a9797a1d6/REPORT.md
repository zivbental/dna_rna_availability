# YNL055C
Status: ok. Length: 931 nt. Measured usable bases: 837. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 837 | 0.3576 | 0.3315 |
| rnafold | ok | 837 | 0.3502 | 0.3423 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 824 | -0.0497 | -0.2024 |
| seed_p | 824 | -0.2621 | -0.2627 |
| seed_p_vs_seed_pars | 789 | -0.3005 | -0.2520 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
