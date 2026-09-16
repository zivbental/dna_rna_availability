# YMR305C
Status: ok. Length: 1461 nt. Measured usable bases: 1239. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1239 | 0.2930 | 0.2727 |
| rnafold | ok | 1239 | 0.2306 | 0.2344 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1125 | -0.1034 | -0.1471 |
| seed_p | 1125 | -0.1795 | -0.1768 |
| seed_p_vs_seed_pars | 1003 | -0.1268 | -0.1853 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
