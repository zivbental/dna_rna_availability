# YLR407W
Status: ok. Length: 1151 nt. Measured usable bases: 401. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 401 | 0.4399 | 0.4255 |
| rnafold | ok | 401 | 0.2759 | 0.2591 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 43 | -0.2231 | 0.2334 |
| seed_p | 43 | -0.4959 | -0.4634 |
| seed_p_vs_seed_pars | 36 | -0.7930 | -0.7182 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
