# YLR056W
Status: ok. Length: 1282 nt. Measured usable bases: 1169. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1169 | 0.2504 | 0.2384 |
| rnafold | ok | 1169 | 0.1729 | 0.1931 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1161 | 0.1119 | 0.2437 |
| seed_p | 1161 | 0.1722 | 0.1636 |
| seed_p_vs_seed_pars | 1128 | 0.0266 | 0.0350 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
