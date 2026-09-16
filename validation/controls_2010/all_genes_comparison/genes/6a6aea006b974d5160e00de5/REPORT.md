# YGR034W
Status: ok. Length: 544 nt. Measured usable bases: 318. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 318 | 0.1295 | 0.0750 |
| rnafold | ok | 318 | 0.1248 | 0.0812 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 162 | 0.0713 | 0.1378 |
| seed_p | 162 | -0.0311 | -0.0450 |
| seed_p_vs_seed_pars | 139 | -0.0491 | -0.1603 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
