# YBL042C
Status: ok. Length: 2138 nt. Measured usable bases: 1145.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1145 | 0.2927 | 0.2720 |
| rnafold | ok | 1145 | 0.2314 | 0.2352 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 203 | -0.1275 | 0.0498 |
| seed_p | 203 | -0.0332 | 0.0711 |
| seed_p_vs_seed_pars | 141 | -0.2765 | -0.2325 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
