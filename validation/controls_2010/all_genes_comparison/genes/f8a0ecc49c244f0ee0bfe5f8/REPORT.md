# YLR090W
Status: ok. Length: 1561 nt. Measured usable bases: 558. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 558 | 0.3096 | 0.3062 |
| rnafold | ok | 558 | 0.2600 | 0.2765 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 59 | 0.1019 | 0.0332 |
| seed_p | 59 | 0.0375 | -0.1918 |
| seed_p_vs_seed_pars | 34 | -0.4469 | -0.5622 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
