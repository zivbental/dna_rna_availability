# YNR053C
Status: ok. Length: 1582 nt. Measured usable bases: 1003. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1003 | 0.3452 | 0.3356 |
| rnafold | ok | 1003 | 0.2483 | 0.2481 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 495 | -0.2185 | -0.3122 |
| seed_p | 495 | -0.2972 | -0.2707 |
| seed_p_vs_seed_pars | 377 | -0.5587 | -0.5850 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
