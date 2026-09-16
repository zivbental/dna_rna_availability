# YCL038C
Status: ok. Length: 1587 nt. Measured usable bases: 554. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 554 | 0.3382 | 0.3222 |
| rnafold | ok | 554 | 0.3085 | 0.3036 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 66 | -0.1544 | -0.4721 |
| seed_p | 66 | -0.0329 | -0.2290 |
| seed_p_vs_seed_pars | 49 | -0.2288 | -0.2884 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
