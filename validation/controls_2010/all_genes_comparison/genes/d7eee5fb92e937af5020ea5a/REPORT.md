# YAL030W
Status: ok. Length: 482 nt. Measured usable bases: 252. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 252 | 0.3542 | 0.3378 |
| rnafold | ok | 252 | 0.2635 | 0.2796 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 117 | -0.1527 | -0.0340 |
| seed_p | 117 | -0.0969 | -0.1668 |
| seed_p_vs_seed_pars | 92 | 0.1148 | -0.0588 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
