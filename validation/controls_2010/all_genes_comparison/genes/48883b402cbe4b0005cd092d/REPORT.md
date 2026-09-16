# YML067C
Status: ok. Length: 1087 nt. Measured usable bases: 765. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 765 | 0.2219 | 0.2168 |
| rnafold | ok | 765 | 0.1773 | 0.1996 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 408 | -0.0960 | -0.0607 |
| seed_p | 408 | -0.0614 | -0.0034 |
| seed_p_vs_seed_pars | 309 | -0.1983 | -0.0875 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
