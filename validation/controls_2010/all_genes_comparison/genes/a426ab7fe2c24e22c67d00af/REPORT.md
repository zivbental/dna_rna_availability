# YER003C
Status: ok. Length: 1375 nt. Measured usable bases: 1160. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1160 | 0.2607 | 0.2467 |
| rnafold | ok | 1160 | 0.1861 | 0.1713 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1082 | -0.1444 | -0.1059 |
| seed_p | 1082 | -0.0702 | -0.0416 |
| seed_p_vs_seed_pars | 972 | -0.1880 | -0.1307 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
