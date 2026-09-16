# YDR152W
Status: ok. Length: 866 nt. Measured usable bases: 491. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 491 | 0.2799 | 0.2947 |
| rnafold | ok | 491 | 0.3224 | 0.3302 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 165 | 0.1225 | 0.2046 |
| seed_p | 165 | 0.1459 | 0.0896 |
| seed_p_vs_seed_pars | 110 | -0.2204 | -0.2549 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
