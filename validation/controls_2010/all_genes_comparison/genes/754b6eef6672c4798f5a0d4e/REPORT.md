# YDL090C
Status: ok. Length: 1327 nt. Measured usable bases: 530. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 530 | 0.3145 | 0.3013 |
| rnafold | ok | 530 | 0.2571 | 0.2594 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 37 | 0.4282 | 0.4434 |
| seed_p | 37 | -0.6496 | -0.5404 |
| seed_p_vs_seed_pars | 30 | -0.6868 | -0.8670 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
