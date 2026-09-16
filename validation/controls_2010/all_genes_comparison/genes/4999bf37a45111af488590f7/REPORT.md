# YGR118W
Status: ok. Length: 636 nt. Measured usable bases: 272. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 272 | 0.3855 | 0.3540 |
| rnafold | ok | 272 | 0.3254 | 0.2598 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 141 | -0.1498 | -0.3307 |
| seed_p | 141 | -0.0661 | -0.4690 |
| seed_p_vs_seed_pars | 128 | -0.4885 | -0.1442 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
