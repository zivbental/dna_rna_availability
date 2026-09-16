# YHR188C
Status: ok. Length: 1922 nt. Measured usable bases: 1424. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1424 | 0.3421 | 0.3143 |
| rnafold | ok | 1424 | 0.2695 | 0.2411 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 966 | -0.1784 | -0.2087 |
| seed_p | 966 | -0.2740 | -0.2368 |
| seed_p_vs_seed_pars | 789 | -0.3849 | -0.2826 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
