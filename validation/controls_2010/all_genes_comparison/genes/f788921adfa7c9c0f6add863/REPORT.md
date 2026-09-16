# YDR099W
Status: ok. Length: 1872 nt. Measured usable bases: 835. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 835 | 0.4008 | 0.3876 |
| rnafold | ok | 835 | 0.2687 | 0.2847 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 540 | -0.2684 | -0.2883 |
| seed_p | 540 | -0.3754 | -0.2995 |
| seed_p_vs_seed_pars | 438 | -0.5377 | -0.4127 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
