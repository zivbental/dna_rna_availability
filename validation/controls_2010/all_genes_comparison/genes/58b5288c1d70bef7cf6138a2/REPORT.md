# YBR263W
Status: ok. Length: 1473 nt. Measured usable bases: 1092. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1092 | 0.2638 | 0.2682 |
| rnafold | ok | 1092 | 0.1665 | 0.1991 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 724 | 0.0720 | 0.0579 |
| seed_p | 724 | -0.0665 | -0.0717 |
| seed_p_vs_seed_pars | 612 | -0.1802 | -0.1589 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
