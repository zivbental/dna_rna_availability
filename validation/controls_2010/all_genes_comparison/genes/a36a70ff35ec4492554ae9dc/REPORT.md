# YNL044W
Status: ok. Length: 752 nt. Measured usable bases: 564. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 564 | 0.2755 | 0.2646 |
| rnafold | ok | 564 | 0.2463 | 0.2550 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 437 | -0.1184 | -0.0486 |
| seed_p | 437 | -0.2020 | -0.1459 |
| seed_p_vs_seed_pars | 369 | -0.2405 | -0.2228 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
