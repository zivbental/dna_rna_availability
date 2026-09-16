# YOL129W
Status: ok. Length: 734 nt. Measured usable bases: 531. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 531 | 0.2573 | 0.2345 |
| rnafold | ok | 531 | 0.2889 | 0.2822 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 426 | 0.0123 | 0.2454 |
| seed_p | 426 | -0.3075 | -0.2829 |
| seed_p_vs_seed_pars | 282 | -0.2621 | -0.3764 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
