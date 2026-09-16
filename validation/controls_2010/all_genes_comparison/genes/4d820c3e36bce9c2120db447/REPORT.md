# YDL219W
Status: ok. Length: 558 nt. Measured usable bases: 316. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 316 | 0.3912 | 0.3762 |
| rnafold | ok | 316 | 0.3111 | 0.2951 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 111 | -0.2309 | -0.4767 |
| seed_p | 111 | -0.2616 | -0.4224 |
| seed_p_vs_seed_pars | 71 | -0.3988 | -0.5166 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
