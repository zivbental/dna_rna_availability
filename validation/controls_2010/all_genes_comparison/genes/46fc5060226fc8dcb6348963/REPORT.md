# YLR061W
Status: ok. Length: 473 nt. Measured usable bases: 417. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 417 | 0.3849 | 0.3855 |
| rnafold | ok | 417 | 0.3888 | 0.4045 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 383 | -0.0623 | -0.3336 |
| seed_p | 383 | -0.3400 | -0.4502 |
| seed_p_vs_seed_pars | 355 | -0.3516 | -0.3855 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
