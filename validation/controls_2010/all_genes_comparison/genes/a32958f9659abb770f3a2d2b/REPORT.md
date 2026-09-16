# YKR071C
Status: ok. Length: 1341 nt. Measured usable bases: 623. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 623 | 0.3045 | 0.3165 |
| rnafold | ok | 623 | 0.2690 | 0.2722 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 112 | -0.3446 | -0.1317 |
| seed_p | 112 | 0.0150 | -0.0791 |
| seed_p_vs_seed_pars | 85 | 0.2562 | 0.0472 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
