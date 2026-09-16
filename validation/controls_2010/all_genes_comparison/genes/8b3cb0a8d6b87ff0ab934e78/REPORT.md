# YPL169C
Status: ok. Length: 2077 nt. Measured usable bases: 1078. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1078 | 0.2365 | 0.2251 |
| rnafold | ok | 1078 | 0.1948 | 0.1871 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 291 | 0.0104 | -0.3126 |
| seed_p | 291 | -0.1259 | -0.1943 |
| seed_p_vs_seed_pars | 213 | -0.1311 | -0.2171 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
