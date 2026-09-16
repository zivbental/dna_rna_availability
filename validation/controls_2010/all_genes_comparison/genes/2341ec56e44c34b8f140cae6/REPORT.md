# YCR088W
Status: ok. Length: 1900 nt. Measured usable bases: 1111. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1111 | 0.3695 | 0.3632 |
| rnafold | ok | 1111 | 0.2924 | 0.3087 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 393 | 0.0444 | -0.0703 |
| seed_p | 393 | -0.2904 | -0.2804 |
| seed_p_vs_seed_pars | 292 | -0.3801 | -0.3994 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
