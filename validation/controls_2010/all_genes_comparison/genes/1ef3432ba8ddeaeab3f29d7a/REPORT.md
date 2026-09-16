# YNL162W
Status: ok. Length: 433 nt. Measured usable bases: 141. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 141 | 0.3958 | 0.3770 |
| rnafold | ok | 141 | 0.3840 | 0.3562 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 63 | -0.3876 | 0.2994 |
| seed_p | 63 | -0.0657 | 0.1447 |
| seed_p_vs_seed_pars | 59 | -0.2213 | 0.1482 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
