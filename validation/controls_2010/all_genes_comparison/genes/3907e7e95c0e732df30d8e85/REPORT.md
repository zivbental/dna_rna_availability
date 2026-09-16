# YDR483W
Status: ok. Length: 1510 nt. Measured usable bases: 1217. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1217 | 0.3114 | 0.3064 |
| rnafold | ok | 1217 | 0.2755 | 0.2897 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1018 | -0.1414 | -0.1053 |
| seed_p | 1018 | -0.1308 | 0.0012 |
| seed_p_vs_seed_pars | 890 | -0.2609 | -0.2234 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
