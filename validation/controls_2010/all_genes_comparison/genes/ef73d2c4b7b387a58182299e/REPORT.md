# YKL140W
Status: ok. Length: 1972 nt. Measured usable bases: 880. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 880 | 0.3294 | 0.3197 |
| rnafold | ok | 880 | 0.3187 | 0.3057 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 98 | -0.4727 | -0.5107 |
| seed_p | 98 | -0.6299 | -0.6125 |
| seed_p_vs_seed_pars | 85 | -0.5498 | -0.5186 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
