# YCR026C
Status: ok. Length: 2507 nt. Measured usable bases: 1129. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1129 | 0.3019 | 0.2939 |
| rnafold | ok | 1129 | 0.2656 | 0.2608 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 179 | -0.2393 | -0.4027 |
| seed_p | 179 | -0.3214 | -0.3276 |
| seed_p_vs_seed_pars | 128 | -0.1365 | -0.1987 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
