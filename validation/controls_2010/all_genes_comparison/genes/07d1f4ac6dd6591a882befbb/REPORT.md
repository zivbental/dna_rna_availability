# YHR205W
Status: ok. Length: 2655 nt. Measured usable bases: 1308. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1308 | 0.3032 | 0.2950 |
| rnafold | ok | 1308 | 0.2224 | 0.2379 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 297 | -0.1324 | -0.4030 |
| seed_p | 297 | -0.3204 | -0.4315 |
| seed_p_vs_seed_pars | 208 | -0.3519 | -0.3758 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
