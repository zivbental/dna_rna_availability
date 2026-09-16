# YER060W
Status: ok. Length: 1854 nt. Measured usable bases: 919. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 919 | 0.2361 | 0.2245 |
| rnafold | ok | 919 | 0.1298 | 0.1359 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 158 | 0.0481 | -0.4070 |
| seed_p | 158 | 0.3010 | 0.1348 |
| seed_p_vs_seed_pars | 132 | 0.2430 | 0.2024 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
