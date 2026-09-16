# YLR208W
Status: ok. Length: 1256 nt. Measured usable bases: 930. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 930 | 0.3043 | 0.2887 |
| rnafold | ok | 930 | 0.2714 | 0.2635 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 727 | -0.1643 | -0.2144 |
| seed_p | 727 | -0.1895 | -0.2660 |
| seed_p_vs_seed_pars | 587 | -0.1898 | -0.2457 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
