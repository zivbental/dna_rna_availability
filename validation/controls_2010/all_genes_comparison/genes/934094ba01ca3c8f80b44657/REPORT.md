# YEL029C
Status: ok. Length: 1094 nt. Measured usable bases: 506. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 506 | 0.2973 | 0.3078 |
| rnafold | ok | 506 | 0.1977 | 0.2395 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 49 | -0.4787 | -0.6512 |
| seed_p | 49 | -0.3187 | -0.3974 |
| seed_p_vs_seed_pars | 39 | -0.3468 | -0.2402 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
