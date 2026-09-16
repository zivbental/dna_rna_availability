# YBL030C
Status: ok. Length: 1323 nt. Measured usable bases: 984.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 984 | 0.2712 | 0.2494 |
| rnafold | ok | 984 | 0.1898 | 0.1659 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 729 | -0.0810 | -0.0173 |
| seed_p | 729 | -0.2225 | -0.1333 |
| seed_p_vs_seed_pars | 628 | -0.2828 | -0.2111 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
