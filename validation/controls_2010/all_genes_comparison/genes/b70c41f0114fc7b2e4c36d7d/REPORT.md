# YGL221C
Status: ok. Length: 1287 nt. Measured usable bases: 776. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 776 | 0.3435 | 0.3325 |
| rnafold | ok | 776 | 0.2900 | 0.2859 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 609 | 0.1464 | 0.0009 |
| seed_p | 609 | 0.0653 | 0.0352 |
| seed_p_vs_seed_pars | 521 | -0.0790 | -0.0697 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
