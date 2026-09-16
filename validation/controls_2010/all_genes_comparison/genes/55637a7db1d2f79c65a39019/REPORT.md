# YML036W
Status: ok. Length: 819 nt. Measured usable bases: 261. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 261 | 0.4027 | 0.3712 |
| rnafold | ok | 261 | 0.3567 | 0.3299 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 30 | 0.2069 | -0.1144 |
| seed_p | 30 | -0.8704 | -0.7774 |
| seed_p_vs_seed_pars | 30 | -0.6791 | -0.5474 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
