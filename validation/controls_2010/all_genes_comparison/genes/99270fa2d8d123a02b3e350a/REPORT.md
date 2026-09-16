# YCR020C-A
Status: ok. Length: 421 nt. Measured usable bases: 273. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 273 | 0.2377 | 0.2381 |
| rnafold | ok | 273 | 0.1819 | 0.1815 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 154 | -0.1676 | -0.0602 |
| seed_p | 154 | -0.1152 | 0.0081 |
| seed_p_vs_seed_pars | 125 | 0.2297 | 0.3633 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
