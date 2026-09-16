# YDL029W
Status: ok. Length: 1313 nt. Measured usable bases: 1044. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1044 | 0.2826 | 0.2728 |
| rnafold | ok | 1044 | 0.2277 | 0.2511 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 973 | -0.0217 | -0.1938 |
| seed_p | 973 | -0.0657 | -0.1871 |
| seed_p_vs_seed_pars | 742 | -0.0608 | -0.1336 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
