# YBR072W
Status: ok. Length: 870 nt. Measured usable bases: 331. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 331 | 0.3473 | 0.3505 |
| rnafold | ok | 331 | 0.2676 | 0.2673 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 57 | -0.0092 | -0.1749 |
| seed_p | 57 | -0.1896 | -0.1598 |
| seed_p_vs_seed_pars | 49 | -0.2162 | 0.1919 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
