# YMR125W
Status: ok. Length: 2803 nt. Measured usable bases: 1424. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1424 | 0.2826 | 0.2804 |
| rnafold | ok | 1424 | 0.1739 | 0.1822 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 406 | -0.0947 | -0.0722 |
| seed_p | 406 | -0.1870 | -0.1554 |
| seed_p_vs_seed_pars | 334 | -0.1949 | -0.1058 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
