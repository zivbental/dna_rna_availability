# YER166W
Status: ok. Length: 4798 nt. Measured usable bases: 1835. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1835 | 0.3029 | 0.2774 |
| rnafold | ok | 1835 | 0.2514 | 0.2390 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 241 | -0.1468 | 0.0007 |
| seed_p | 241 | -0.1188 | -0.1668 |
| seed_p_vs_seed_pars | 171 | -0.2924 | -0.3692 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
