# YDL191W
Status: ok. Length: 513 nt. Measured usable bases: 130. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 130 | 0.3231 | 0.3723 |
| rnafold | ok | 130 | 0.2747 | 0.3049 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 95 | -0.4190 | -0.3808 |
| seed_p | 95 | -0.6449 | -0.5882 |
| seed_p_vs_seed_pars | 73 | -0.6995 | -0.4878 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
