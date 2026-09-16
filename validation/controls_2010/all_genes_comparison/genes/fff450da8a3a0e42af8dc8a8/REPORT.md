# YJL001W
Status: ok. Length: 803 nt. Measured usable bases: 655. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 655 | 0.3240 | 0.3200 |
| rnafold | ok | 655 | 0.1994 | 0.1899 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 579 | -0.0402 | -0.2878 |
| seed_p | 579 | -0.1002 | -0.1238 |
| seed_p_vs_seed_pars | 521 | -0.0862 | -0.1140 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
