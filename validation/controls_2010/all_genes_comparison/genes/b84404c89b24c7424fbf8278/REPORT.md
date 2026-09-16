# YML073C
Status: ok. Length: 609 nt. Measured usable bases: 433. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 433 | 0.4228 | 0.4161 |
| rnafold | ok | 433 | 0.3981 | 0.4085 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 322 | -0.2560 | -0.3727 |
| seed_p | 322 | -0.3755 | -0.2966 |
| seed_p_vs_seed_pars | 278 | -0.1251 | -0.0967 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
