# YPL129W
Status: ok. Length: 896 nt. Measured usable bases: 518. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 518 | 0.3391 | 0.3363 |
| rnafold | ok | 518 | 0.2960 | 0.2964 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 196 | -0.1964 | -0.0611 |
| seed_p | 196 | 0.0232 | 0.0231 |
| seed_p_vs_seed_pars | 142 | -0.2215 | -0.1413 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
