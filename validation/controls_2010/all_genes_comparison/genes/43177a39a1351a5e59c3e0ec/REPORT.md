# YCL010C
Status: ok. Length: 873 nt. Measured usable bases: 484. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 484 | 0.4342 | 0.4249 |
| rnafold | ok | 484 | 0.4253 | 0.4133 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 123 | 0.1403 | 0.3399 |
| seed_p | 123 | 0.2368 | 0.2254 |
| seed_p_vs_seed_pars | 101 | 0.0877 | 0.1119 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
