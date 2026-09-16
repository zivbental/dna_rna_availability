# YER007C-A
Status: ok. Length: 741 nt. Measured usable bases: 404. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 404 | 0.2634 | 0.2636 |
| rnafold | ok | 404 | 0.2487 | 0.2580 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 114 | -0.4554 | -0.5202 |
| seed_p | 114 | -0.3681 | -0.2842 |
| seed_p_vs_seed_pars | 79 | -0.4086 | -0.2928 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
