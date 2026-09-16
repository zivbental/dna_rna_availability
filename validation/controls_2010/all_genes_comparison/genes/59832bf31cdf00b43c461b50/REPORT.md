# YPL079W
Status: ok. Length: 616 nt. Measured usable bases: 306. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 306 | 0.1834 | 0.1860 |
| rnafold | ok | 306 | 0.1803 | 0.1982 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 179 | -0.0864 | -0.0884 |
| seed_p | 179 | -0.1054 | -0.0769 |
| seed_p_vs_seed_pars | 155 | 0.0085 | 0.1162 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
