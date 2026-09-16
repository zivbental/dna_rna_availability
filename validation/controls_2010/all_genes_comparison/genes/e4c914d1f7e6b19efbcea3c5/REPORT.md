# YHR010W
Status: ok. Length: 558 nt. Measured usable bases: 404. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 404 | 0.3535 | 0.3420 |
| rnafold | ok | 404 | 0.3374 | 0.3478 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 314 | -0.0933 | -0.1578 |
| seed_p | 314 | -0.3752 | -0.4457 |
| seed_p_vs_seed_pars | 266 | -0.5122 | -0.4424 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
