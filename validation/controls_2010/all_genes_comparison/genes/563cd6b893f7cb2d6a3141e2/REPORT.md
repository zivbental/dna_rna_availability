# YLR190W
Status: ok. Length: 1906 nt. Measured usable bases: 1071. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1071 | 0.3159 | 0.3323 |
| rnafold | ok | 1071 | 0.3032 | 0.3142 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 300 | -0.0205 | 0.2518 |
| seed_p | 300 | 0.0552 | 0.0390 |
| seed_p_vs_seed_pars | 223 | -0.0206 | 0.0160 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
