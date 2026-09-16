# YCL002C
Status: ok. Length: 898 nt. Measured usable bases: 488. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 488 | 0.1581 | 0.1436 |
| rnafold | ok | 488 | 0.1500 | 0.1268 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 116 | 0.1086 | 0.3203 |
| seed_p | 116 | 0.1107 | 0.1073 |
| seed_p_vs_seed_pars | 73 | -0.1122 | -0.1880 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
