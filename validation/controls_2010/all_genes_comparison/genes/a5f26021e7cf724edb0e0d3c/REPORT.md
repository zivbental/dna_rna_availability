# YNL265C
Status: ok. Length: 1176 nt. Measured usable bases: 406. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 406 | 0.3999 | 0.3912 |
| rnafold | ok | 406 | 0.3108 | 0.2900 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 40 | -0.2940 | -0.3717 |
| seed_p | 40 | -0.4205 | -0.4405 |
| seed_p_vs_seed_pars | 32 | -0.2934 | -0.7632 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
