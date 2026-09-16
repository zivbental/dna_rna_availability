# YOL120C
Status: ok. Length: 651 nt. Measured usable bases: 255. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 255 | 0.3728 | 0.3694 |
| rnafold | ok | 255 | 0.2198 | 0.2458 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 137 | -0.0468 | -0.3574 |
| seed_p | 137 | 0.2092 | 0.1283 |
| seed_p_vs_seed_pars | 101 | -0.0613 | -0.0341 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
