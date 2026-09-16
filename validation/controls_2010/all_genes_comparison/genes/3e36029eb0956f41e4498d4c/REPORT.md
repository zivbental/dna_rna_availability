# YPL050C
Status: ok. Length: 1445 nt. Measured usable bases: 982. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 982 | 0.2915 | 0.2905 |
| rnafold | ok | 982 | 0.2527 | 0.2635 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 547 | 0.1096 | -0.2665 |
| seed_p | 547 | -0.0986 | -0.1897 |
| seed_p_vs_seed_pars | 369 | -0.3017 | -0.4344 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
