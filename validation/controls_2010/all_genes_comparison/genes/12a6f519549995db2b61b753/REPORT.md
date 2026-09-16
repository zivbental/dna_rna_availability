# YLR185W
Status: ok. Length: 385 nt. Measured usable bases: 267. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 267 | 0.3184 | 0.3237 |
| rnafold | ok | 267 | 0.2934 | 0.3091 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 225 | 0.1188 | -0.1085 |
| seed_p | 225 | -0.1578 | -0.1046 |
| seed_p_vs_seed_pars | 203 | -0.0150 | -0.0078 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
