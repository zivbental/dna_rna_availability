# YOR182C
Status: ok. Length: 249 nt. Measured usable bases: 125. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 125 | 0.5767 | 0.5698 |
| rnafold | ok | 125 | 0.4472 | 0.4345 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 65 | -0.4532 | -0.6677 |
| seed_p | 65 | -0.6989 | -0.7644 |
| seed_p_vs_seed_pars | 54 | -0.7269 | -0.9090 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
