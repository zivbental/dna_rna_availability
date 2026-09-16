# YCL047C
Status: ok. Length: 868 nt. Measured usable bases: 341. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 341 | 0.2967 | 0.2713 |
| rnafold | ok | 341 | 0.1687 | 0.1541 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 48 | 0.5496 | 0.1685 |
| seed_p | 48 | 0.4537 | 0.4179 |
| seed_p_vs_seed_pars | 20 | -0.0616 | -0.0308 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
