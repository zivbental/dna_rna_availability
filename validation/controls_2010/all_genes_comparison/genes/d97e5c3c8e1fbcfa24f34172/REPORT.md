# YLR219W
Status: ok. Length: 2519 nt. Measured usable bases: 1029. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1029 | 0.3258 | 0.3287 |
| rnafold | ok | 1029 | 0.2811 | 0.2790 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 163 | -0.4738 | -0.4049 |
| seed_p | 163 | -0.4900 | -0.4550 |
| seed_p_vs_seed_pars | 91 | -0.0972 | -0.0639 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
