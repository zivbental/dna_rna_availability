# YDR524C-B
Status: ok. Length: 361 nt. Measured usable bases: 312. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 312 | 0.3919 | 0.3997 |
| rnafold | ok | 312 | 0.3816 | 0.4010 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 281 | -0.3713 | -0.3863 |
| seed_p | 281 | -0.5149 | -0.4459 |
| seed_p_vs_seed_pars | 239 | -0.3704 | -0.4484 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
