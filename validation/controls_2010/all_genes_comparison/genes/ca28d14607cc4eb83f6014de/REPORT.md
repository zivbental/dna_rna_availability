# YNL038W
Status: ok. Length: 786 nt. Measured usable bases: 351. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 351 | 0.3265 | 0.3275 |
| rnafold | ok | 351 | 0.1947 | 0.2171 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 44 | 0.5986 | 0.6007 |
| seed_p | 44 | 0.4121 | 0.4327 |
| seed_p_vs_seed_pars | 22 | 0.1438 | -0.2049 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
