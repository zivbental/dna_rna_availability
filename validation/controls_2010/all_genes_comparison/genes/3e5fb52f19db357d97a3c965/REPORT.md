# YFL039C
Status: ok. Length: 1338 nt. Measured usable bases: 1262. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1262 | 0.2790 | 0.2568 |
| rnafold | ok | 1262 | 0.2427 | 0.2344 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1254 | -0.0119 | -0.0548 |
| seed_p | 1254 | -0.0559 | -0.0182 |
| seed_p_vs_seed_pars | 1195 | -0.1568 | -0.0695 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
