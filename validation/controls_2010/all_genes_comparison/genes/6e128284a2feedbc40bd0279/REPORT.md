# YML024W
Status: ok. Length: 552 nt. Measured usable bases: 234. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 234 | 0.2907 | 0.3107 |
| rnafold | ok | 234 | 0.3136 | 0.3097 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 71 | -0.5323 | -0.7546 |
| seed_p | 71 | 0.0725 | -0.1942 |
| seed_p_vs_seed_pars | 69 | -0.1678 | -0.2912 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
