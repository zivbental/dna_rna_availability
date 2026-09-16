# YKR082W
Status: ok. Length: 3576 nt. Measured usable bases: 1314. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1314 | 0.2839 | 0.2802 |
| rnafold | ok | 1314 | 0.2431 | 0.2484 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 39 | -0.3917 | -0.3280 |
| seed_p | 39 | -0.4385 | -0.4304 |
| seed_p_vs_seed_pars | 38 | -0.7224 | -0.7584 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
