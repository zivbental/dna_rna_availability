# YNL301C
Status: ok. Length: 729 nt. Measured usable bases: 286. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 286 | 0.3265 | 0.3559 |
| rnafold | ok | 286 | 0.2401 | 0.2711 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 127 | -0.4861 | 0.0647 |
| seed_p | 127 | -0.2029 | -0.1065 |
| seed_p_vs_seed_pars | 106 | -0.2809 | -0.2069 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
