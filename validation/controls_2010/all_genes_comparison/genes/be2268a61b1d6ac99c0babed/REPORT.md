# YOR122C
Status: ok. Length: 582 nt. Measured usable bases: 492. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 492 | 0.3863 | 0.3860 |
| rnafold | ok | 492 | 0.2363 | 0.2574 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 465 | -0.2103 | -0.4231 |
| seed_p | 465 | -0.2965 | -0.3216 |
| seed_p_vs_seed_pars | 430 | -0.2095 | -0.2983 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
