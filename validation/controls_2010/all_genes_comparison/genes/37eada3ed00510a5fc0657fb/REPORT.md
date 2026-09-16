# YBR189W
Status: ok. Length: 682 nt. Measured usable bases: 444. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 444 | 0.4240 | 0.4082 |
| rnafold | ok | 444 | 0.3312 | 0.3359 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 294 | -0.1368 | -0.4349 |
| seed_p | 294 | -0.3127 | -0.2170 |
| seed_p_vs_seed_pars | 266 | -0.3526 | -0.3144 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
