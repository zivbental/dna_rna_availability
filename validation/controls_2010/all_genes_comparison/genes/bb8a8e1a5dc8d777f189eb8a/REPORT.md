# YGR255C
Status: ok. Length: 1730 nt. Measured usable bases: 803. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 803 | 0.3220 | 0.2882 |
| rnafold | ok | 803 | 0.2028 | 0.1643 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 101 | 0.0431 | 0.0158 |
| seed_p | 101 | -0.1118 | -0.1041 |
| seed_p_vs_seed_pars | 75 | -0.3180 | -0.1398 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
