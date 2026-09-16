# YMR119W
Status: ok. Length: 2096 nt. Measured usable bases: 973. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 973 | 0.2530 | 0.2486 |
| rnafold | ok | 973 | 0.1784 | 0.1905 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 129 | -0.3532 | -0.4896 |
| seed_p | 129 | -0.3646 | -0.4187 |
| seed_p_vs_seed_pars | 84 | -0.4814 | -0.4314 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
