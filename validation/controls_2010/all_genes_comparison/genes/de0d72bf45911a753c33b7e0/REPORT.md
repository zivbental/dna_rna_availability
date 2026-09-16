# YPL218W
Status: ok. Length: 689 nt. Measured usable bases: 616. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 616 | 0.2106 | 0.1799 |
| rnafold | ok | 616 | 0.1550 | 0.1286 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 599 | -0.0392 | -0.1206 |
| seed_p | 599 | 0.0280 | 0.0128 |
| seed_p_vs_seed_pars | 537 | -0.0292 | -0.0158 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
