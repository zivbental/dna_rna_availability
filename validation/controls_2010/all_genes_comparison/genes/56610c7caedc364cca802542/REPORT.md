# YOL121C
Status: ok. Length: 537 nt. Measured usable bases: 237. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 237 | 0.3343 | 0.3080 |
| rnafold | ok | 237 | 0.2077 | 0.1761 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 91 | -0.2307 | -0.3078 |
| seed_p | 91 | -0.1089 | -0.2086 |
| seed_p_vs_seed_pars | 70 | 0.0599 | -0.2287 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
