# YJL055W
Status: ok. Length: 822 nt. Measured usable bases: 570. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 570 | 0.3833 | 0.3571 |
| rnafold | ok | 570 | 0.3323 | 0.3121 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 297 | -0.2474 | -0.4032 |
| seed_p | 297 | -0.2794 | -0.2539 |
| seed_p_vs_seed_pars | 225 | -0.2737 | -0.2874 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
