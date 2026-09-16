# YJR148W
Status: ok. Length: 1240 nt. Measured usable bases: 1026. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1026 | 0.3255 | 0.3123 |
| rnafold | ok | 1026 | 0.2396 | 0.2170 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 934 | 0.0143 | -0.0113 |
| seed_p | 934 | -0.2431 | -0.1703 |
| seed_p_vs_seed_pars | 828 | -0.3023 | -0.2542 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
