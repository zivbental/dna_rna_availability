# YNL016W
Status: ok. Length: 2010 nt. Measured usable bases: 1154. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1154 | 0.2221 | 0.2209 |
| rnafold | ok | 1154 | 0.1928 | 0.2106 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 565 | 0.0832 | -0.0188 |
| seed_p | 565 | 0.0227 | 0.0561 |
| seed_p_vs_seed_pars | 438 | -0.0407 | -0.0484 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
