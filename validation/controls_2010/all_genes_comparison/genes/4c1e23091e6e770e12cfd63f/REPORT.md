# YMR116C
Status: ok. Length: 1122 nt. Measured usable bases: 1061. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1061 | 0.3863 | 0.3545 |
| rnafold | ok | 1061 | 0.3424 | 0.3300 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1017 | -0.2839 | -0.1056 |
| seed_p | 1017 | -0.2508 | -0.1214 |
| seed_p_vs_seed_pars | 1012 | -0.2258 | -0.1997 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
