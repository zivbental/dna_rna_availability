# YBR191W
Status: ok. Length: 510 nt. Measured usable bases: 207. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 207 | 0.3876 | 0.3222 |
| rnafold | ok | 207 | 0.3956 | 0.3777 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 95 | -0.6884 | -0.3093 |
| seed_p | 95 | -0.4101 | -0.2732 |
| seed_p_vs_seed_pars | 60 | -0.3617 | -0.2681 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
