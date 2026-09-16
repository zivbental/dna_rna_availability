# YER078C
Status: ok. Length: 1659 nt. Measured usable bases: 660. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 660 | 0.3371 | 0.3255 |
| rnafold | ok | 660 | 0.2311 | 0.2333 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 35 | 0.4094 | 0.3115 |
| seed_p | 35 | 0.5796 | 0.4793 |
| seed_p_vs_seed_pars | 23 | 0.2239 | 0.0153 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
