# YAL013W
Status: ok. Length: 1338 nt. Measured usable bases: 469. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 469 | 0.3339 | 0.3314 |
| rnafold | ok | 469 | 0.3286 | 0.3226 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 26 | 0.4109 | 0.4816 |
| seed_p | 26 | -0.3871 | -0.2644 |
| seed_p_vs_seed_pars | 16 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
