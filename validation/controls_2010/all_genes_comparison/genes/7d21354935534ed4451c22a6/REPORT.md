# YJR105W
Status: ok. Length: 1103 nt. Measured usable bases: 1013. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1013 | 0.2980 | 0.2567 |
| rnafold | ok | 1013 | 0.2558 | 0.2308 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 965 | -0.1552 | 0.0110 |
| seed_p | 965 | -0.1376 | 0.0183 |
| seed_p_vs_seed_pars | 938 | -0.2119 | -0.0259 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
