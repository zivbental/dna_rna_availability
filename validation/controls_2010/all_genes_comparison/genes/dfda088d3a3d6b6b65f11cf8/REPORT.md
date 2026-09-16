# YDR471W
Status: ok. Length: 550 nt. Measured usable bases: 384. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 384 | 0.3236 | 0.3376 |
| rnafold | ok | 384 | 0.3078 | 0.3103 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 288 | -0.0634 | -0.0354 |
| seed_p | 288 | -0.2411 | -0.2753 |
| seed_p_vs_seed_pars | 208 | -0.5925 | -0.4493 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
