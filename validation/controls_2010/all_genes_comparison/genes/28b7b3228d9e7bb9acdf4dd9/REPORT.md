# YKL112W
Status: ok. Length: 3571 nt. Measured usable bases: 1006. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1006 | 0.2796 | 0.2765 |
| rnafold | ok | 1006 | 0.1975 | 0.1980 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 162 | -0.0722 | 0.2412 |
| seed_p | 162 | 0.1887 | 0.2822 |
| seed_p_vs_seed_pars | 101 | 0.0814 | 0.2397 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
