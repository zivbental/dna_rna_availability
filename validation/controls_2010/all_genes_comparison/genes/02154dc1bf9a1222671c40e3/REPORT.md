# YKL190W
Status: ok. Length: 731 nt. Measured usable bases: 388. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 388 | 0.3694 | 0.3493 |
| rnafold | ok | 388 | 0.3295 | 0.3076 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 113 | 0.1223 | -0.0508 |
| seed_p | 113 | -0.0413 | -0.1622 |
| seed_p_vs_seed_pars | 68 | -0.2409 | -0.2992 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
