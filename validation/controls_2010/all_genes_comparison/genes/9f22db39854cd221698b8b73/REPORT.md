# YDL064W
Status: ok. Length: 594 nt. Measured usable bases: 367. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 367 | 0.3145 | 0.2975 |
| rnafold | ok | 367 | 0.1847 | 0.1674 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 213 | -0.2518 | -0.1653 |
| seed_p | 213 | -0.0084 | -0.0111 |
| seed_p_vs_seed_pars | 165 | -0.0367 | -0.1140 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
