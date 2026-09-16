# YOR316C
Status: ok. Length: 1565 nt. Measured usable bases: 715. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 715 | 0.2658 | 0.2372 |
| rnafold | ok | 715 | 0.2405 | 0.2106 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 252 | 0.1221 | 0.1947 |
| seed_p | 252 | 0.1707 | 0.1778 |
| seed_p_vs_seed_pars | 142 | -0.0249 | -0.0522 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
