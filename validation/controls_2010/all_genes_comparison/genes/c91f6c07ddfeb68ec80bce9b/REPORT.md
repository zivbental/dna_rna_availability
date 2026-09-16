# YOR312C
Status: ok. Length: 588 nt. Measured usable bases: 270. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 270 | 0.3108 | 0.2877 |
| rnafold | ok | 270 | 0.3446 | 0.3357 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 151 | -0.2132 | -0.5058 |
| seed_p | 151 | -0.3204 | -0.4957 |
| seed_p_vs_seed_pars | 120 | -0.3754 | -0.5562 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
