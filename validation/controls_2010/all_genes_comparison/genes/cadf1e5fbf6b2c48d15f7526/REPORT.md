# YOR336W
Status: ok. Length: 4334 nt. Measured usable bases: 1399. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1399 | 0.3233 | 0.3137 |
| rnafold | ok | 1399 | 0.2846 | 0.2811 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 67 | -0.4172 | -0.2721 |
| seed_p | 67 | -0.3634 | -0.5306 |
| seed_p_vs_seed_pars | 59 | -0.5941 | -0.6751 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
