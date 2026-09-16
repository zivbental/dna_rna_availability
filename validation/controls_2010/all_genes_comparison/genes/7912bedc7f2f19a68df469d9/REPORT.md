# YGR141W
Status: ok. Length: 1549 nt. Measured usable bases: 616. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 616 | 0.3526 | 0.3478 |
| rnafold | ok | 616 | 0.2615 | 0.2978 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 67 | 0.4530 | 0.0956 |
| seed_p | 67 | -0.1210 | -0.2342 |
| seed_p_vs_seed_pars | 47 | 0.0677 | -0.1587 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
