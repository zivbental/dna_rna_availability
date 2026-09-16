# YHR016C
Status: ok. Length: 1563 nt. Measured usable bases: 746. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 746 | 0.3518 | 0.3379 |
| rnafold | ok | 746 | 0.2635 | 0.2682 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 98 | 0.1492 | 0.5745 |
| seed_p | 98 | 0.2993 | 0.3174 |
| seed_p_vs_seed_pars | 59 | 0.2117 | 0.3336 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
