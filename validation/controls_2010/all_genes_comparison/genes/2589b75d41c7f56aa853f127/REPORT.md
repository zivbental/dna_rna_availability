# YPL075W
Status: ok. Length: 2594 nt. Measured usable bases: 988. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 988 | 0.2944 | 0.2864 |
| rnafold | ok | 988 | 0.2577 | 0.2460 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 96 | -0.0193 | -0.0434 |
| seed_p | 96 | 0.0128 | 0.0997 |
| seed_p_vs_seed_pars | 78 | -0.2632 | -0.1740 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
