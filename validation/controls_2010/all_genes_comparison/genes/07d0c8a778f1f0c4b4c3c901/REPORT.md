# YER005W
Status: ok. Length: 1984 nt. Measured usable bases: 1077. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1077 | 0.3069 | 0.2951 |
| rnafold | ok | 1077 | 0.2910 | 0.2816 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 239 | -0.0591 | -0.2019 |
| seed_p | 239 | -0.6379 | -0.6024 |
| seed_p_vs_seed_pars | 160 | -0.7141 | -0.6565 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
