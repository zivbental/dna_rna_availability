# YJL177W
Status: ok. Length: 690 nt. Measured usable bases: 448. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 448 | 0.3028 | 0.3069 |
| rnafold | ok | 448 | 0.2788 | 0.2896 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 305 | -0.1845 | -0.1683 |
| seed_p | 305 | -0.1751 | -0.1609 |
| seed_p_vs_seed_pars | 272 | -0.1076 | -0.0937 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
