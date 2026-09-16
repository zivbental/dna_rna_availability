# YBR009C
Status: ok. Length: 484 nt. Measured usable bases: 227.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 227 | 0.2260 | 0.2312 |
| rnafold | ok | 227 | 0.2443 | 0.2688 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 133 | -0.2824 | -0.3275 |
| seed_p | 133 | -0.5748 | -0.5745 |
| seed_p_vs_seed_pars | 87 | -0.3825 | -0.2066 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
