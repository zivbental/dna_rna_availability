# YBR062C
Status: ok. Length: 637 nt. Measured usable bases: 284. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 284 | 0.3011 | 0.2934 |
| rnafold | ok | 284 | 0.2730 | 0.2634 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 46 | -0.6276 | -0.2946 |
| seed_p | 46 | 0.0834 | 0.0557 |
| seed_p_vs_seed_pars | 37 | -0.0362 | 0.0757 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
