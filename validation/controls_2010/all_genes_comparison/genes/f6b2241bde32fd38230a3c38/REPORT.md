# YDL082W
Status: ok. Length: 769 nt. Measured usable bases: 488. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 488 | 0.3371 | 0.3130 |
| rnafold | ok | 488 | 0.3288 | 0.3352 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 333 | -0.1155 | -0.2462 |
| seed_p | 333 | -0.0722 | -0.1340 |
| seed_p_vs_seed_pars | 248 | -0.5933 | -0.4748 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
