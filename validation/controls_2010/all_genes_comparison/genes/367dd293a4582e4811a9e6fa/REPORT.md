# YCR057C
Status: ok. Length: 2999 nt. Measured usable bases: 1623. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1623 | 0.2918 | 0.2852 |
| rnafold | ok | 1623 | 0.1765 | 0.1881 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 297 | -0.0347 | -0.1613 |
| seed_p | 297 | -0.1229 | -0.1551 |
| seed_p_vs_seed_pars | 211 | -0.1923 | -0.1047 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
