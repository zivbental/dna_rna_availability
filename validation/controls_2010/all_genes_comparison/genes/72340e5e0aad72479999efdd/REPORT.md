# YOR254C
Status: ok. Length: 2191 nt. Measured usable bases: 1527. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1527 | 0.2811 | 0.2690 |
| rnafold | ok | 1527 | 0.2055 | 0.2159 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 976 | 0.0089 | -0.0501 |
| seed_p | 976 | -0.0610 | -0.0395 |
| seed_p_vs_seed_pars | 672 | -0.1919 | -0.1249 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
