# YJL034W
Status: ok. Length: 2286 nt. Measured usable bases: 1904. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1904 | 0.2849 | 0.2703 |
| rnafold | ok | 1904 | 0.2629 | 0.2410 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1658 | 0.0078 | 0.0733 |
| seed_p | 1658 | 0.0484 | 0.0291 |
| seed_p_vs_seed_pars | 1436 | -0.0898 | -0.1146 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
