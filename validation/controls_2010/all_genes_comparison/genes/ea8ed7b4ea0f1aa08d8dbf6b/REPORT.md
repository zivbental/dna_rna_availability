# YDR260C
Status: ok. Length: 696 nt. Measured usable bases: 329. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 329 | 0.3932 | 0.3769 |
| rnafold | ok | 329 | 0.3274 | 0.3554 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 43 | 0.1161 | -0.2291 |
| seed_p | 43 | 0.5400 | 0.5867 |
| seed_p_vs_seed_pars | 40 | 0.8571 | 0.9226 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
