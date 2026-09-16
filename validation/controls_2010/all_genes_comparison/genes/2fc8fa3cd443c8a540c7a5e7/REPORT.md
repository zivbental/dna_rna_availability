# YDL006W
Status: ok. Length: 1296 nt. Measured usable bases: 553. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 553 | 0.1949 | 0.2071 |
| rnafold | ok | 553 | 0.1424 | 0.1558 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 67 | 0.3053 | 0.6008 |
| seed_p | 67 | -0.0426 | 0.0710 |
| seed_p_vs_seed_pars | 58 | -0.0304 | 0.0195 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
