# YGL030W
Status: ok. Length: 464 nt. Measured usable bases: 427. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 427 | 0.1933 | 0.1758 |
| rnafold | ok | 427 | 0.2012 | 0.2244 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 409 | -0.0338 | -0.0811 |
| seed_p | 409 | -0.1018 | -0.1490 |
| seed_p_vs_seed_pars | 407 | -0.0682 | -0.0565 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
