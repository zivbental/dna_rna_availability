# YFL031W
Status: ok. Length: 1201 nt. Measured usable bases: 1032. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1032 | 0.3893 | 0.3945 |
| rnafold | ok | 1032 | 0.2808 | 0.2497 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 931 | -0.1394 | -0.4228 |
| seed_p | 931 | -0.3555 | -0.3878 |
| seed_p_vs_seed_pars | 854 | -0.3158 | -0.4353 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
