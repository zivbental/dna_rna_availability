# YML056C
Status: ok. Length: 1935 nt. Measured usable bases: 1300. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1300 | 0.3217 | 0.3019 |
| rnafold | ok | 1300 | 0.2498 | 0.2215 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1151 | -0.0194 | -0.0267 |
| seed_p | 1151 | -0.0929 | -0.0149 |
| seed_p_vs_seed_pars | 1018 | -0.0848 | -0.0372 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
