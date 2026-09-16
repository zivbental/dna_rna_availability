# YJL184W
Status: ok. Length: 476 nt. Measured usable bases: 219. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 219 | 0.4607 | 0.4590 |
| rnafold | ok | 219 | 0.3942 | 0.4043 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 92 | 0.0864 | 0.0402 |
| seed_p | 92 | -0.3409 | -0.2550 |
| seed_p_vs_seed_pars | 73 | -0.6850 | -0.6718 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
