# YOL125W
Status: ok. Length: 1514 nt. Measured usable bases: 656. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 656 | 0.3911 | 0.3811 |
| rnafold | ok | 656 | 0.3232 | 0.3316 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 118 | -0.3818 | -0.4313 |
| seed_p | 118 | -0.3629 | -0.3560 |
| seed_p_vs_seed_pars | 101 | -0.5946 | -0.5487 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
