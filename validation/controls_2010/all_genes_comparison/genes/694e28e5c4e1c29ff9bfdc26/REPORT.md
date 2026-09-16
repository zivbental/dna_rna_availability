# YER019C-A
Status: ok. Length: 347 nt. Measured usable bases: 265. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 265 | 0.3555 | 0.3443 |
| rnafold | ok | 265 | 0.3636 | 0.3549 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 251 | 0.2649 | 0.1312 |
| seed_p | 251 | 0.0906 | -0.0283 |
| seed_p_vs_seed_pars | 239 | -0.1153 | -0.1216 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
