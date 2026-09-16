# YPL049C
Status: ok. Length: 1628 nt. Measured usable bases: 905. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 905 | 0.3623 | 0.3464 |
| rnafold | ok | 905 | 0.1678 | 0.1812 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 173 | 0.0157 | 0.0642 |
| seed_p | 173 | 0.1830 | 0.1127 |
| seed_p_vs_seed_pars | 112 | 0.1228 | 0.0219 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
