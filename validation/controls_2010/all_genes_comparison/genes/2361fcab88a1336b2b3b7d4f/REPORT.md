# YDR222W
Status: ok. Length: 1471 nt. Measured usable bases: 666. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 666 | 0.3116 | 0.3169 |
| rnafold | ok | 666 | 0.3284 | 0.3309 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 87 | 0.0013 | 0.1058 |
| seed_p | 87 | -0.2126 | -0.0413 |
| seed_p_vs_seed_pars | 60 | -0.3263 | 0.0288 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
