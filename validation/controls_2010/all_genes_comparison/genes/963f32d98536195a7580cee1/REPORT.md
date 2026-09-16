# YGR012W
Status: ok. Length: 1346 nt. Measured usable bases: 621. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 621 | 0.4173 | 0.4132 |
| rnafold | ok | 621 | 0.2712 | 0.2801 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 57 | 0.1788 | -0.3759 |
| seed_p | 57 | 0.4371 | 0.2809 |
| seed_p_vs_seed_pars | 50 | 0.1180 | 0.0333 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
