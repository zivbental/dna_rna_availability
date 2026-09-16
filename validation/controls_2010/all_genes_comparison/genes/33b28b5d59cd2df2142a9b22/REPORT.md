# YJL024C
Status: ok. Length: 823 nt. Measured usable bases: 418. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 418 | 0.2811 | 0.2994 |
| rnafold | ok | 418 | 0.3132 | 0.3215 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 109 | -0.1794 | -0.4713 |
| seed_p | 109 | -0.6414 | -0.5615 |
| seed_p_vs_seed_pars | 67 | -0.5422 | -0.5638 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
