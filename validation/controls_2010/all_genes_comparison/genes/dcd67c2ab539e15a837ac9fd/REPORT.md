# YPL006W
Status: ok. Length: 3629 nt. Measured usable bases: 1358. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1358 | 0.3147 | 0.2987 |
| rnafold | ok | 1358 | 0.2106 | 0.2144 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 118 | -0.2055 | 0.1013 |
| seed_p | 118 | -0.1704 | -0.1204 |
| seed_p_vs_seed_pars | 55 | 0.0160 | 0.1978 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
