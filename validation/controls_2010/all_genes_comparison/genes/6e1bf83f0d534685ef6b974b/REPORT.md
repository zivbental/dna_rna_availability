# YML026C
Status: ok. Length: 644 nt. Measured usable bases: 260. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 260 | 0.2885 | 0.2864 |
| rnafold | ok | 260 | 0.2206 | 0.2145 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 164 | 0.4451 | -0.1004 |
| seed_p | 164 | 0.1613 | 0.0263 |
| seed_p_vs_seed_pars | 153 | 0.1887 | 0.1340 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
