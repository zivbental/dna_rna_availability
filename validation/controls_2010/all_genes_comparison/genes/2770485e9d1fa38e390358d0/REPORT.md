# YHR021C
Status: ok. Length: 360 nt. Measured usable bases: 300. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 300 | 0.3048 | 0.2743 |
| rnafold | ok | 300 | 0.3546 | 0.3394 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 252 | -0.0503 | 0.2974 |
| seed_p | 252 | -0.0307 | 0.1878 |
| seed_p_vs_seed_pars | 241 | -0.4070 | -0.1139 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
