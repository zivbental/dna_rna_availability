# YCR075W-A
Status: ok. Length: 343 nt. Measured usable bases: 141. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 141 | 0.3414 | 0.3157 |
| rnafold | ok | 141 | 0.2254 | 0.1966 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 42 | -0.6410 | -0.6057 |
| seed_p | 42 | -0.6073 | -0.4172 |
| seed_p_vs_seed_pars | 28 | -0.1057 | -0.2027 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
