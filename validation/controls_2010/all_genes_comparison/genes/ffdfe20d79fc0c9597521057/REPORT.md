# YJL078C
Status: ok. Length: 2894 nt. Measured usable bases: 1858. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1858 | 0.2288 | 0.2093 |
| rnafold | ok | 1858 | 0.2171 | 0.2053 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 820 | -0.1463 | -0.0601 |
| seed_p | 820 | -0.1670 | -0.1208 |
| seed_p_vs_seed_pars | 660 | -0.1591 | -0.1701 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
