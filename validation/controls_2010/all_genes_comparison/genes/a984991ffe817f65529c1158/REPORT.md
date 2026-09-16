# YLR350W
Status: ok. Length: 783 nt. Measured usable bases: 529. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 529 | 0.2310 | 0.2075 |
| rnafold | ok | 529 | 0.1950 | 0.1697 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 359 | -0.1932 | 0.1896 |
| seed_p | 359 | -0.0908 | -0.0515 |
| seed_p_vs_seed_pars | 284 | -0.0790 | 0.0392 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
