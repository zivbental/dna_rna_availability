# YBR149W
Status: ok. Length: 1166 nt. Measured usable bases: 928. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 928 | 0.3709 | 0.3516 |
| rnafold | ok | 928 | 0.3121 | 0.3166 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 736 | 0.0186 | 0.0498 |
| seed_p | 736 | -0.1966 | -0.1855 |
| seed_p_vs_seed_pars | 587 | -0.2120 | -0.2084 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
