# YPR010C-A
Status: ok. Length: 474 nt. Measured usable bases: 187. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 187 | 0.3292 | 0.3224 |
| rnafold | ok | 187 | 0.3200 | 0.2964 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 48 | -0.8118 | -0.6138 |
| seed_p | 48 | -0.1155 | -0.0713 |
| seed_p_vs_seed_pars | 47 | -0.2188 | -0.5114 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
