# YIL133C
Status: ok. Length: 717 nt. Measured usable bases: 540. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 540 | 0.2887 | 0.2793 |
| rnafold | ok | 540 | 0.2552 | 0.2677 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 476 | -0.0182 | -0.1085 |
| seed_p | 476 | -0.3652 | -0.2568 |
| seed_p_vs_seed_pars | 385 | -0.4423 | -0.3417 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
