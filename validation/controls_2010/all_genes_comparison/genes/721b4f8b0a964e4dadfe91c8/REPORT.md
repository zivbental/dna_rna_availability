# YBL040C
Status: ok. Length: 761 nt. Measured usable bases: 569. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 569 | 0.2937 | 0.2790 |
| rnafold | ok | 569 | 0.1834 | 0.1645 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 486 | -0.1551 | -0.0383 |
| seed_p | 486 | -0.2442 | 0.0037 |
| seed_p_vs_seed_pars | 396 | -0.0890 | 0.1681 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
