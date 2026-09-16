# YJL059W
Status: ok. Length: 1418 nt. Measured usable bases: 540. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 540 | 0.1780 | 0.1609 |
| rnafold | ok | 540 | 0.1997 | 0.1909 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 65 | -0.4654 | -0.1101 |
| seed_p | 65 | 0.2420 | 0.2608 |
| seed_p_vs_seed_pars | 50 | 0.6627 | 0.6296 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
