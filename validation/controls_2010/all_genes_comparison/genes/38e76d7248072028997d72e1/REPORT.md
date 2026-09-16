# YDR188W
Status: ok. Length: 1855 nt. Measured usable bases: 1398. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1398 | 0.3702 | 0.3615 |
| rnafold | ok | 1398 | 0.2938 | 0.3130 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1124 | -0.0562 | -0.1142 |
| seed_p | 1124 | -0.1579 | -0.1844 |
| seed_p_vs_seed_pars | 909 | -0.3542 | -0.2780 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
