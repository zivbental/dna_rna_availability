# YCR031C
Status: ok. Length: 514 nt. Measured usable bases: 303. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 303 | 0.3361 | 0.3144 |
| rnafold | ok | 303 | 0.1616 | 0.1832 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 212 | 0.0149 | 0.5331 |
| seed_p | 212 | -0.2294 | 0.1702 |
| seed_p_vs_seed_pars | 201 | -0.3009 | 0.1253 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
