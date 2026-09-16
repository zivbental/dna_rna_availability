# YLR375W
Status: ok. Length: 1124 nt. Measured usable bases: 865. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 865 | 0.3703 | 0.3673 |
| rnafold | ok | 865 | 0.2671 | 0.2759 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 628 | -0.1323 | -0.3193 |
| seed_p | 628 | -0.4192 | -0.4456 |
| seed_p_vs_seed_pars | 491 | -0.5105 | -0.5034 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
