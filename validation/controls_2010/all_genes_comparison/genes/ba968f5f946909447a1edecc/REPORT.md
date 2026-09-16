# YPL273W
Status: ok. Length: 1189 nt. Measured usable bases: 728. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 728 | 0.3879 | 0.3701 |
| rnafold | ok | 728 | 0.3700 | 0.3573 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 574 | -0.1234 | -0.2326 |
| seed_p | 574 | -0.1644 | -0.2666 |
| seed_p_vs_seed_pars | 481 | -0.3261 | -0.4205 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
