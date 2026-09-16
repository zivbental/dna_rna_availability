# YOR206W
Status: ok. Length: 2229 nt. Measured usable bases: 1129. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1129 | 0.3129 | 0.3140 |
| rnafold | ok | 1129 | 0.2530 | 0.2505 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 255 | 0.0596 | 0.3028 |
| seed_p | 255 | 0.0222 | -0.0144 |
| seed_p_vs_seed_pars | 167 | -0.2808 | -0.3126 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
