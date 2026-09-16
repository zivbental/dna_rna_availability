# YDR064W
Status: ok. Length: 561 nt. Measured usable bases: 515. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 515 | 0.2407 | 0.2585 |
| rnafold | ok | 515 | 0.1725 | 0.1780 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 487 | -0.0326 | -0.1483 |
| seed_p | 487 | -0.2520 | -0.2668 |
| seed_p_vs_seed_pars | 479 | -0.2392 | -0.3196 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
