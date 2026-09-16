# YDL018C
Status: ok. Length: 824 nt. Measured usable bases: 418. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 418 | 0.2984 | 0.2839 |
| rnafold | ok | 418 | 0.3324 | 0.3014 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 97 | -0.1121 | 0.1322 |
| seed_p | 97 | 0.0952 | 0.1608 |
| seed_p_vs_seed_pars | 92 | -0.1971 | -0.0626 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
