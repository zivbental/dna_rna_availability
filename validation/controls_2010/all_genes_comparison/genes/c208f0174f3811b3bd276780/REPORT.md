# YOR278W
Status: ok. Length: 828 nt. Measured usable bases: 363. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 363 | 0.2881 | 0.2764 |
| rnafold | ok | 363 | 0.2984 | 0.2843 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 28 | 0.6033 | 0.8019 |
| seed_p | 28 | 0.4493 | 0.1948 |
| seed_p_vs_seed_pars | 17 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
