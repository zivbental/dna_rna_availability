# YMR033W
Status: ok. Length: 1589 nt. Measured usable bases: 723. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 723 | 0.3216 | 0.2924 |
| rnafold | ok | 723 | 0.2439 | 0.2349 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 110 | 0.3699 | 0.0987 |
| seed_p | 110 | 0.0465 | 0.1723 |
| seed_p_vs_seed_pars | 65 | -0.1901 | -0.0955 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
