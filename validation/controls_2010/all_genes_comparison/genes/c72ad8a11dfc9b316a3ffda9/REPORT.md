# YLR448W
Status: ok. Length: 844 nt. Measured usable bases: 561. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 561 | 0.2646 | 0.2516 |
| rnafold | ok | 561 | 0.2218 | 0.2197 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 350 | -0.0408 | 0.0240 |
| seed_p | 350 | -0.0631 | -0.1716 |
| seed_p_vs_seed_pars | 310 | -0.1041 | -0.1937 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
