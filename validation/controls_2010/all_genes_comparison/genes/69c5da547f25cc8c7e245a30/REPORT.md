# YDR500C
Status: ok. Length: 342 nt. Measured usable bases: 222. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 222 | 0.3386 | 0.3339 |
| rnafold | ok | 222 | 0.3578 | 0.3598 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 174 | -0.1041 | -0.0081 |
| seed_p | 174 | 0.0403 | 0.0435 |
| seed_p_vs_seed_pars | 167 | 0.1961 | 0.2019 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
