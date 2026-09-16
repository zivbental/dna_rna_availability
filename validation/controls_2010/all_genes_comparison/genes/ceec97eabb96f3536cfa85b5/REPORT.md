# YJL072C
Status: ok. Length: 642 nt. Measured usable bases: 324. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 324 | 0.2773 | 0.2607 |
| rnafold | ok | 324 | 0.1962 | 0.1865 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 36 | -0.2085 | -0.3800 |
| seed_p | 36 | -0.7589 | -0.5824 |
| seed_p_vs_seed_pars | 28 | -0.9284 | -0.8934 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
