# YHR065C
Status: ok. Length: 1622 nt. Measured usable bases: 746. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 746 | 0.3294 | 0.3263 |
| rnafold | ok | 746 | 0.2408 | 0.2430 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 127 | -0.0614 | 0.0596 |
| seed_p | 127 | 0.0255 | 0.0870 |
| seed_p_vs_seed_pars | 88 | -0.3207 | -0.3538 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
