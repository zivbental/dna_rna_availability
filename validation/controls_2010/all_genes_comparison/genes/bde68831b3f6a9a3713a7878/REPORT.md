# YLL050C
Status: ok. Length: 547 nt. Measured usable bases: 488. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 488 | 0.3531 | 0.3296 |
| rnafold | ok | 488 | 0.3279 | 0.2919 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 475 | 0.0316 | 0.0250 |
| seed_p | 475 | -0.3697 | -0.2588 |
| seed_p_vs_seed_pars | 461 | -0.5167 | -0.3534 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
