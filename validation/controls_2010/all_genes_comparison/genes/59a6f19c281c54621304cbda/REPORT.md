# YOR361C
Status: ok. Length: 2358 nt. Measured usable bases: 1898. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1898 | 0.3169 | 0.3007 |
| rnafold | ok | 1898 | 0.2533 | 0.2490 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1652 | -0.0316 | -0.1982 |
| seed_p | 1652 | -0.1596 | -0.1887 |
| seed_p_vs_seed_pars | 1386 | -0.1789 | -0.1738 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
