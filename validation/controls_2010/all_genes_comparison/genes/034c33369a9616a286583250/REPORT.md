# YBL026W
Status: ok. Length: 481 nt. Measured usable bases: 247. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 247 | 0.3021 | 0.3039 |
| rnafold | ok | 247 | 0.2877 | 0.3026 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 44 | -0.1064 | -0.2844 |
| seed_p | 44 | 0.5819 | 0.5647 |
| seed_p_vs_seed_pars | 32 | 0.1599 | -0.2532 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
