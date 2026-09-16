# YGL137W
Status: ok. Length: 2880 nt. Measured usable bases: 2003. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2003 | 0.3328 | 0.3231 |
| rnafold | ok | 2003 | 0.2994 | 0.2951 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1145 | -0.0890 | -0.1256 |
| seed_p | 1145 | -0.3175 | -0.2813 |
| seed_p_vs_seed_pars | 901 | -0.4098 | -0.3950 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
