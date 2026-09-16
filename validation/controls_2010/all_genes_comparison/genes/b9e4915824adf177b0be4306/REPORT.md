# YDL014W
Status: ok. Length: 1328 nt. Measured usable bases: 1036. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1036 | 0.2204 | 0.2053 |
| rnafold | ok | 1036 | 0.1897 | 0.2159 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 918 | -0.1444 | -0.1109 |
| seed_p | 918 | -0.1858 | -0.1853 |
| seed_p_vs_seed_pars | 796 | -0.2195 | -0.2739 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
