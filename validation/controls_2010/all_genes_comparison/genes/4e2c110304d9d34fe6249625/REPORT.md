# YLR179C
Status: ok. Length: 705 nt. Measured usable bases: 634. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 634 | 0.3277 | 0.3175 |
| rnafold | ok | 634 | 0.2523 | 0.2713 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 626 | 0.0421 | 0.0077 |
| seed_p | 626 | -0.1894 | -0.1014 |
| seed_p_vs_seed_pars | 600 | -0.2697 | -0.2741 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
