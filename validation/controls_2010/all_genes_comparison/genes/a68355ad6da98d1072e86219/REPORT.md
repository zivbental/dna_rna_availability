# YEL054C
Status: ok. Length: 714 nt. Measured usable bases: 458. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 458 | 0.2683 | 0.2577 |
| rnafold | ok | 458 | 0.2810 | 0.2975 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 342 | -0.0046 | -0.1896 |
| seed_p | 342 | -0.2664 | -0.2835 |
| seed_p_vs_seed_pars | 315 | -0.1207 | -0.0857 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
