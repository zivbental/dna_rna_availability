# YHR076W
Status: ok. Length: 1176 nt. Measured usable bases: 547. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 547 | 0.3401 | 0.3473 |
| rnafold | ok | 547 | 0.2676 | 0.3016 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 109 | -0.2319 | -0.3078 |
| seed_p | 109 | -0.4373 | -0.3291 |
| seed_p_vs_seed_pars | 100 | -0.6113 | -0.4000 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
