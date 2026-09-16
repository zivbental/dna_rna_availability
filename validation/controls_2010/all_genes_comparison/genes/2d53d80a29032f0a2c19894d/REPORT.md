# YJL127C-B
Status: ok. Length: 560 nt. Measured usable bases: 345. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 345 | 0.3186 | 0.3192 |
| rnafold | ok | 345 | 0.3501 | 0.3638 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 155 | 0.0162 | 0.1853 |
| seed_p | 155 | -0.0131 | 0.0577 |
| seed_p_vs_seed_pars | 122 | -0.1805 | 0.0294 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
