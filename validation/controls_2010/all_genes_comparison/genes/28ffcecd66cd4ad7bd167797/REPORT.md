# YNL112W
Status: ok. Length: 1801 nt. Measured usable bases: 1366. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1366 | 0.4004 | 0.4054 |
| rnafold | ok | 1366 | 0.3738 | 0.3768 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1063 | -0.0403 | -0.3122 |
| seed_p | 1063 | -0.1556 | -0.2667 |
| seed_p_vs_seed_pars | 808 | -0.3687 | -0.3547 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
