# YCL059C
Status: ok. Length: 1070 nt. Measured usable bases: 506. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 506 | 0.3896 | 0.3787 |
| rnafold | ok | 506 | 0.3613 | 0.3578 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 107 | 0.1448 | 0.2082 |
| seed_p | 107 | -0.0328 | 0.0668 |
| seed_p_vs_seed_pars | 73 | -0.1233 | 0.0107 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
