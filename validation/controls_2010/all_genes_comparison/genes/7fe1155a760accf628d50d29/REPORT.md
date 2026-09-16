# YML004C
Status: ok. Length: 1169 nt. Measured usable bases: 871. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 871 | 0.2928 | 0.2839 |
| rnafold | ok | 871 | 0.2414 | 0.2415 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 691 | -0.1201 | -0.0965 |
| seed_p | 691 | -0.1426 | -0.0629 |
| seed_p_vs_seed_pars | 565 | -0.1977 | -0.1277 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
