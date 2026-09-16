# YBL087C
Status: ok. Length: 504 nt. Measured usable bases: 249. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 249 | 0.2640 | 0.2588 |
| rnafold | ok | 249 | 0.3021 | 0.3332 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 148 | -0.3217 | -0.5454 |
| seed_p | 148 | -0.6038 | -0.4879 |
| seed_p_vs_seed_pars | 129 | -0.3882 | -0.1958 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
