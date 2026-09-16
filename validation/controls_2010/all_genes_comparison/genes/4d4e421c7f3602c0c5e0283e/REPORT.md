# YPL101W
Status: ok. Length: 1488 nt. Measured usable bases: 800. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 800 | 0.3396 | 0.3317 |
| rnafold | ok | 800 | 0.3263 | 0.3158 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 165 | 0.2007 | 0.1851 |
| seed_p | 165 | 0.0230 | 0.0647 |
| seed_p_vs_seed_pars | 118 | -0.1577 | -0.1310 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
