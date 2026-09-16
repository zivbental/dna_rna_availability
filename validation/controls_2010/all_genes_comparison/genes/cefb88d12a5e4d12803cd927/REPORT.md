# YDR139C
Status: ok. Length: 413 nt. Measured usable bases: 252. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 252 | 0.3845 | 0.3914 |
| rnafold | ok | 252 | 0.3339 | 0.3218 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 90 | -0.0090 | 0.0394 |
| seed_p | 90 | -0.1440 | -0.0776 |
| seed_p_vs_seed_pars | 41 | -0.3964 | -0.5215 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
