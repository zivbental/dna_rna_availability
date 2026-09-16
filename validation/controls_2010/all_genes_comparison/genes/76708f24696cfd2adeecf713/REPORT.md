# YDR025W
Status: ok. Length: 577 nt. Measured usable bases: 276. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 276 | 0.2342 | 0.2197 |
| rnafold | ok | 276 | 0.1658 | 0.1527 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 124 | 0.0075 | -0.1085 |
| seed_p | 124 | 0.2148 | 0.0933 |
| seed_p_vs_seed_pars | 112 | 0.1248 | -0.0107 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
