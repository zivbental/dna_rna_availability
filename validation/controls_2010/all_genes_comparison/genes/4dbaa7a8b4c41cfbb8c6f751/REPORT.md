# YGR106C
Status: ok. Length: 929 nt. Measured usable bases: 761. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 761 | 0.2519 | 0.2610 |
| rnafold | ok | 761 | 0.2093 | 0.2112 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 750 | -0.1279 | -0.2970 |
| seed_p | 750 | -0.1551 | -0.3033 |
| seed_p_vs_seed_pars | 653 | -0.1066 | -0.1884 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
