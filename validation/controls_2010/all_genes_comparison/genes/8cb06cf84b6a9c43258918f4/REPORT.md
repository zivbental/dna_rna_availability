# YOR096W
Status: ok. Length: 695 nt. Measured usable bases: 482. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 482 | 0.4047 | 0.3804 |
| rnafold | ok | 482 | 0.2950 | 0.2818 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 407 | -0.2412 | -0.4173 |
| seed_p | 407 | -0.4707 | -0.4809 |
| seed_p_vs_seed_pars | 383 | -0.5868 | -0.5156 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
