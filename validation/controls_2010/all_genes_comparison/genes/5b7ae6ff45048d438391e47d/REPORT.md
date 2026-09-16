# YHR012W
Status: ok. Length: 1332 nt. Measured usable bases: 582. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 582 | 0.4464 | 0.4499 |
| rnafold | ok | 582 | 0.3014 | 0.2889 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 130 | -0.2680 | -0.3958 |
| seed_p | 130 | -0.2682 | -0.3858 |
| seed_p_vs_seed_pars | 90 | -0.5269 | -0.5539 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
