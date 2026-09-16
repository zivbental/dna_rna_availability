# YER133W
Status: ok. Length: 1228 nt. Measured usable bases: 762. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 762 | 0.3358 | 0.3313 |
| rnafold | ok | 762 | 0.2671 | 0.2737 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 290 | -0.0553 | -0.0789 |
| seed_p | 290 | -0.3332 | -0.1005 |
| seed_p_vs_seed_pars | 244 | -0.1927 | -0.0126 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
