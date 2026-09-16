# YLR212C
Status: ok. Length: 1723 nt. Measured usable bases: 823. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 823 | 0.2391 | 0.2234 |
| rnafold | ok | 823 | 0.2432 | 0.2337 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 156 | 0.1915 | 0.1064 |
| seed_p | 156 | 0.1753 | 0.0449 |
| seed_p_vs_seed_pars | 138 | -0.2139 | -0.3506 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
