# YLR074C
Status: ok. Length: 568 nt. Measured usable bases: 399. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 399 | 0.3495 | 0.3536 |
| rnafold | ok | 399 | 0.3415 | 0.3559 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 282 | -0.1913 | -0.0545 |
| seed_p | 282 | -0.1433 | -0.1802 |
| seed_p_vs_seed_pars | 239 | -0.2792 | -0.3685 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
