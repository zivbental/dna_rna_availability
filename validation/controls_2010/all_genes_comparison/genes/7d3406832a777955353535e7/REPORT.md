# YJL104W
Status: ok. Length: 649 nt. Measured usable bases: 353. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 353 | 0.3458 | 0.3519 |
| rnafold | ok | 353 | 0.3084 | 0.3360 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 99 | -0.2049 | -0.1831 |
| seed_p | 99 | -0.1210 | -0.1479 |
| seed_p_vs_seed_pars | 67 | -0.3169 | -0.4251 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
