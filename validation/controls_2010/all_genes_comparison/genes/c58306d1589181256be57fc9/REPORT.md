# YLR244C
Status: ok. Length: 1323 nt. Measured usable bases: 964. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 964 | 0.3453 | 0.3214 |
| rnafold | ok | 964 | 0.2866 | 0.2824 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 769 | -0.0076 | -0.1232 |
| seed_p | 769 | -0.1600 | -0.1362 |
| seed_p_vs_seed_pars | 701 | -0.2674 | -0.1991 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
