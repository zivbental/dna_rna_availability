# YNL291C
Status: ok. Length: 1954 nt. Measured usable bases: 1165. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1165 | 0.2854 | 0.2667 |
| rnafold | ok | 1165 | 0.2583 | 0.2339 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 405 | 0.0236 | -0.2604 |
| seed_p | 405 | -0.4027 | -0.2621 |
| seed_p_vs_seed_pars | 271 | -0.6474 | -0.5087 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
