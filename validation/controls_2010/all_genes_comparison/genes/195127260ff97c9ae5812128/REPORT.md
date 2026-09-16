# YFR045W
Status: ok. Length: 1052 nt. Measured usable bases: 380. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 380 | 0.3715 | 0.3674 |
| rnafold | ok | 380 | 0.1772 | 0.1634 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 34 | 0.7732 | 0.7042 |
| seed_p | 34 | -0.2822 | -0.1709 |
| seed_p_vs_seed_pars | 31 | -0.4654 | -0.2201 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
