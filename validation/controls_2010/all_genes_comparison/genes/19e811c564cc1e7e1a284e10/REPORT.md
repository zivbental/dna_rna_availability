# YHR001W-A
Status: ok. Length: 509 nt. Measured usable bases: 250. Mapping: verified_annotated_exons_and_UTRs.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 250 | 0.3213 | 0.3054 |
| rnafold | ok | 250 | 0.3388 | 0.3207 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 68 | -0.4705 | -0.0216 |
| seed_p | 68 | -0.4036 | -0.3778 |
| seed_p_vs_seed_pars | 46 | -0.4438 | -0.4844 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
