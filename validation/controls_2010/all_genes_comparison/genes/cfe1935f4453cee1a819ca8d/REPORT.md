# YPL086C
Status: ok. Length: 1794 nt. Measured usable bases: 1029. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1029 | 0.2907 | 0.2801 |
| rnafold | ok | 1029 | 0.2276 | 0.2165 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 352 | -0.0054 | -0.1510 |
| seed_p | 352 | -0.1008 | -0.0018 |
| seed_p_vs_seed_pars | 272 | -0.3750 | -0.1448 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
