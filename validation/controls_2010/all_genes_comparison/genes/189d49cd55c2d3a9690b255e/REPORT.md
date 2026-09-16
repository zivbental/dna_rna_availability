# YOL048C
Status: ok. Length: 1144 nt. Measured usable bases: 503. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 503 | 0.3482 | 0.3460 |
| rnafold | ok | 503 | 0.3707 | 0.3711 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 56 | -0.2679 | -0.6577 |
| seed_p | 56 | -0.5317 | -0.4590 |
| seed_p_vs_seed_pars | 40 | -0.4727 | -0.3145 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
