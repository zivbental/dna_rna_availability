# YPL240C
Status: ok. Length: 2264 nt. Measured usable bases: 1203. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1203 | 0.3406 | 0.3246 |
| rnafold | ok | 1203 | 0.2866 | 0.2885 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 401 | -0.0022 | -0.2572 |
| seed_p | 401 | -0.2241 | -0.1826 |
| seed_p_vs_seed_pars | 276 | -0.1918 | -0.2855 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
