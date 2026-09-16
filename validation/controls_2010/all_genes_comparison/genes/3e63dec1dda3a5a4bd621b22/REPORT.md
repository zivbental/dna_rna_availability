# YNR032C-A
Status: ok. Length: 329 nt. Measured usable bases: 141. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 141 | 0.4896 | 0.4885 |
| rnafold | ok | 141 | 0.4808 | 0.4651 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 25 | 0.1928 | 0.4113 |
| seed_p | 25 | -0.5598 | -0.5282 |
| seed_p_vs_seed_pars | 25 | -0.9930 | -1.0000 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
