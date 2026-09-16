# YER010C
Status: ok. Length: 876 nt. Measured usable bases: 509. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 509 | 0.2458 | 0.2519 |
| rnafold | ok | 509 | 0.2332 | 0.2574 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 249 | 0.1614 | -0.1678 |
| seed_p | 249 | 0.1076 | 0.0695 |
| seed_p_vs_seed_pars | 187 | -0.2890 | -0.4521 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
