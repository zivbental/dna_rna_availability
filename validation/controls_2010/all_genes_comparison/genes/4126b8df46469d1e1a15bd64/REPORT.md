# YJR040W
Status: ok. Length: 2443 nt. Measured usable bases: 1084. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1084 | 0.3106 | 0.2790 |
| rnafold | ok | 1084 | 0.2271 | 0.2175 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 72 | 0.5406 | 0.3243 |
| seed_p | 72 | 0.2743 | 0.3874 |
| seed_p_vs_seed_pars | 32 | -0.5376 | -0.5305 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
