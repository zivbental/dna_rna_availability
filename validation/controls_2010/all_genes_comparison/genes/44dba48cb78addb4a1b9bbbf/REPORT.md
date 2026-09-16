# YLR367W
Status: ok. Length: 1017 nt. Measured usable bases: 448. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 448 | 0.3330 | 0.3117 |
| rnafold | ok | 448 | 0.2755 | 0.2672 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 218 | 0.0272 | 0.0334 |
| seed_p | 218 | -0.0119 | 0.0390 |
| seed_p_vs_seed_pars | 133 | -0.1874 | 0.0054 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
