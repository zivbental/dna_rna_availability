# YKR057W
Status: ok. Length: 477 nt. Measured usable bases: 349. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 349 | 0.3425 | 0.3305 |
| rnafold | ok | 349 | 0.3366 | 0.3244 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 283 | -0.0407 | -0.0809 |
| seed_p | 283 | -0.1670 | -0.1370 |
| seed_p_vs_seed_pars | 267 | -0.0948 | -0.1390 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
