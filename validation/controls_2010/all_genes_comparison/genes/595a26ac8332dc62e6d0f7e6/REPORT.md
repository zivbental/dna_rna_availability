# YGR193C
Status: ok. Length: 1409 nt. Measured usable bases: 739. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 739 | 0.2626 | 0.2362 |
| rnafold | ok | 739 | 0.2212 | 0.2029 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 121 | 0.1086 | -0.0037 |
| seed_p | 121 | 0.0987 | 0.0439 |
| seed_p_vs_seed_pars | 74 | 0.0473 | 0.1090 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
