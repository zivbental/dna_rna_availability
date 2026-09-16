# YGL226C-A
Status: ok. Length: 418 nt. Measured usable bases: 260. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 260 | 0.1684 | 0.1457 |
| rnafold | ok | 260 | 0.2657 | 0.2741 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 127 | 0.1222 | 0.2823 |
| seed_p | 127 | 0.0136 | -0.0068 |
| seed_p_vs_seed_pars | 114 | 0.0245 | -0.1339 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
