# YGL167C
Status: ok. Length: 3111 nt. Measured usable bases: 2049. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2049 | 0.2744 | 0.2633 |
| rnafold | ok | 2049 | 0.2442 | 0.2359 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 878 | 0.0581 | 0.0417 |
| seed_p | 878 | -0.0252 | -0.0857 |
| seed_p_vs_seed_pars | 660 | -0.1621 | -0.1735 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
