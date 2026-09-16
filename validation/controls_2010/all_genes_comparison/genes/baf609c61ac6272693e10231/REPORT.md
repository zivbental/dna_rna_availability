# YFR024C-A
Status: ok. Length: 1533 nt. Measured usable bases: 1150. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1150 | 0.3508 | 0.3566 |
| rnafold | ok | 1150 | 0.2981 | 0.3032 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 774 | 0.0169 | -0.2260 |
| seed_p | 774 | -0.1240 | -0.1680 |
| seed_p_vs_seed_pars | 634 | -0.1885 | -0.2473 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
