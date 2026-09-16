# YGR055W
Status: ok. Length: 1870 nt. Measured usable bases: 1437. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1437 | 0.2173 | 0.2254 |
| rnafold | ok | 1437 | 0.1953 | 0.2099 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1002 | 0.0826 | -0.1051 |
| seed_p | 1002 | -0.0416 | -0.0593 |
| seed_p_vs_seed_pars | 806 | -0.0715 | -0.1166 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
