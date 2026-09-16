# YBR014C
Status: ok. Length: 760 nt. Measured usable bases: 436. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 436 | 0.3089 | 0.3080 |
| rnafold | ok | 436 | 0.3676 | 0.3811 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 172 | -0.1095 | -0.1967 |
| seed_p | 172 | -0.1897 | -0.1873 |
| seed_p_vs_seed_pars | 116 | 0.0333 | 0.0294 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
