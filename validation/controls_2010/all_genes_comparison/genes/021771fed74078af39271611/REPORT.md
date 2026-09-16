# YOR187W
Status: ok. Length: 1509 nt. Measured usable bases: 1207. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1207 | 0.2875 | 0.2833 |
| rnafold | ok | 1207 | 0.2256 | 0.2268 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1023 | 0.1255 | -0.0091 |
| seed_p | 1023 | -0.0514 | -0.1021 |
| seed_p_vs_seed_pars | 851 | -0.2116 | -0.2395 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
