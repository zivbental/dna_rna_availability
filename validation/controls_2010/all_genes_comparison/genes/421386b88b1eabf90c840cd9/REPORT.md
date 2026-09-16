# YIL064W
Status: ok. Length: 855 nt. Measured usable bases: 416. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 416 | -0.0066 | -0.0310 |
| rnafold | ok | 416 | -0.0149 | -0.0122 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 138 | 0.0294 | 0.1633 |
| seed_p | 138 | -0.4112 | -0.4317 |
| seed_p_vs_seed_pars | 116 | -0.5741 | -0.4576 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
