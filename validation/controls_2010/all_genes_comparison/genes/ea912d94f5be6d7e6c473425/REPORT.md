# YOR116C
Status: ok. Length: 4727 nt. Measured usable bases: 2479. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2479 | 0.3212 | 0.3034 |
| rnafold | ok | 2479 | 0.2338 | 0.2043 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 555 | 0.0183 | 0.0115 |
| seed_p | 555 | 0.0579 | 0.0231 |
| seed_p_vs_seed_pars | 400 | -0.0229 | -0.0569 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
