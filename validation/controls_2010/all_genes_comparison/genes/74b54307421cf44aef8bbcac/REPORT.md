# YGR017W
Status: ok. Length: 1157 nt. Measured usable bases: 543. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 543 | 0.3100 | 0.3181 |
| rnafold | ok | 543 | 0.3398 | 0.3431 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 89 | -0.4296 | -0.3774 |
| seed_p | 89 | -0.1335 | -0.0073 |
| seed_p_vs_seed_pars | 63 | -0.1780 | 0.1681 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
