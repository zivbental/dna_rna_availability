# YCR018C
Status: ok. Length: 806 nt. Measured usable bases: 217. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 217 | 0.4351 | 0.4313 |
| rnafold | ok | 217 | 0.3246 | 0.3576 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 25 | 0.4038 | 0.8213 |
| seed_p | 25 | -0.1245 | 0.0885 |
| seed_p_vs_seed_pars | 16 | undefined | undefined |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
