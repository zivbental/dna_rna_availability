# YJL136C
Status: ok. Length: 405 nt. Measured usable bases: 251. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 251 | 0.4673 | 0.4465 |
| rnafold | ok | 251 | 0.5236 | 0.5118 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 151 | -0.3168 | -0.3198 |
| seed_p | 151 | -0.3599 | -0.3690 |
| seed_p_vs_seed_pars | 122 | -0.4408 | -0.1939 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
