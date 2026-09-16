# YML124C
Status: ok. Length: 1470 nt. Measured usable bases: 1059. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1059 | 0.3086 | 0.2995 |
| rnafold | ok | 1059 | 0.2772 | 0.2776 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 696 | -0.0660 | -0.0926 |
| seed_p | 696 | -0.0726 | -0.0857 |
| seed_p_vs_seed_pars | 572 | -0.1547 | -0.1560 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
