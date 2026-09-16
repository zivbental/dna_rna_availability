# YIL109C
Status: ok. Length: 2966 nt. Measured usable bases: 2106. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2106 | 0.2628 | 0.2387 |
| rnafold | ok | 2106 | 0.2383 | 0.2266 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1890 | 0.0064 | -0.0426 |
| seed_p | 1890 | -0.0771 | -0.0498 |
| seed_p_vs_seed_pars | 1520 | -0.2238 | -0.1602 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
