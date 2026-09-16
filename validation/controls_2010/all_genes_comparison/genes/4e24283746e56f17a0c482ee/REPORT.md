# YGR183C
Status: ok. Length: 618 nt. Measured usable bases: 411. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 411 | 0.1068 | 0.1128 |
| rnafold | ok | 411 | 0.1088 | 0.1248 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 264 | -0.2484 | -0.0579 |
| seed_p | 264 | -0.1729 | -0.1340 |
| seed_p_vs_seed_pars | 217 | -0.3051 | -0.0548 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
