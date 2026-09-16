# YDR092W
Status: ok. Length: 621 nt. Measured usable bases: 414. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 414 | 0.3379 | 0.3387 |
| rnafold | ok | 414 | 0.2753 | 0.2672 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 272 | -0.1956 | -0.2429 |
| seed_p | 272 | -0.1940 | -0.1702 |
| seed_p_vs_seed_pars | 234 | -0.3094 | -0.1619 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
