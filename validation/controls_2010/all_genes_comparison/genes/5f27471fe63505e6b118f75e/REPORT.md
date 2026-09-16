# YGR001C
Status: ok. Length: 800 nt. Measured usable bases: 499. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 499 | 0.2976 | 0.3164 |
| rnafold | ok | 499 | 0.2700 | 0.3120 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 246 | 0.1549 | 0.2455 |
| seed_p | 246 | 0.0278 | 0.2276 |
| seed_p_vs_seed_pars | 196 | 0.0804 | 0.2094 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
