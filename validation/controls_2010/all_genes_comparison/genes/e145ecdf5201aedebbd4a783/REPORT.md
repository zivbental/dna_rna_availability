# YKL081W
Status: ok. Length: 1474 nt. Measured usable bases: 1347. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1347 | 0.3293 | 0.3027 |
| rnafold | ok | 1347 | 0.2983 | 0.2908 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1321 | -0.0196 | -0.1542 |
| seed_p | 1321 | -0.3065 | -0.2215 |
| seed_p_vs_seed_pars | 1260 | -0.3650 | -0.2556 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
