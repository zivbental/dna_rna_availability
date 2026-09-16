# YDR059C
Status: ok. Length: 590 nt. Measured usable bases: 286. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 286 | 0.3605 | 0.3457 |
| rnafold | ok | 286 | 0.2983 | 0.2732 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 51 | -0.7541 | -0.8639 |
| seed_p | 51 | -0.6038 | -0.6022 |
| seed_p_vs_seed_pars | 41 | -0.5261 | -0.3223 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
