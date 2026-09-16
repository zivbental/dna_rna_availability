# YPL250C
Status: ok. Length: 642 nt. Measured usable bases: 321. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 321 | 0.2292 | 0.2477 |
| rnafold | ok | 321 | 0.1711 | 0.1855 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 138 | -0.2419 | -0.1110 |
| seed_p | 138 | -0.2405 | -0.2349 |
| seed_p_vs_seed_pars | 117 | -0.3023 | -0.0873 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
