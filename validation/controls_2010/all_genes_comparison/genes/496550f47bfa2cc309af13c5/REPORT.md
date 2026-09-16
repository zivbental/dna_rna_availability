# YCL009C
Status: ok. Length: 1003 nt. Measured usable bases: 911. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 911 | 0.2980 | 0.2774 |
| rnafold | ok | 911 | 0.1934 | 0.1940 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 879 | 0.0239 | -0.0324 |
| seed_p | 879 | -0.1541 | -0.0388 |
| seed_p_vs_seed_pars | 811 | -0.1623 | -0.0303 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
