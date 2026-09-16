# YGR192C
Status: ok. Length: 1129 nt. Measured usable bases: 262. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 262 | 0.1951 | 0.1841 |
| rnafold | ok | 262 | 0.1902 | 0.1764 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 135 | 0.0053 | -0.1895 |
| seed_p | 135 | 0.2482 | 0.0603 |
| seed_p_vs_seed_pars | 107 | 0.3608 | 0.0932 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
