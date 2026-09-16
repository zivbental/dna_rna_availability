# YDR129C
Status: ok. Length: 2108 nt. Measured usable bases: 1622. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1622 | 0.2786 | 0.2740 |
| rnafold | ok | 1622 | 0.2318 | 0.2439 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1242 | 0.0167 | 0.0644 |
| seed_p | 1242 | -0.0419 | -0.0442 |
| seed_p_vs_seed_pars | 1000 | -0.1208 | -0.0744 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
