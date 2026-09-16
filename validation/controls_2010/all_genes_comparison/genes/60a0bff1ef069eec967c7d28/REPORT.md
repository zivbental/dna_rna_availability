# YOR337W
Status: ok. Length: 2300 nt. Measured usable bases: 840. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 840 | 0.3416 | 0.3317 |
| rnafold | ok | 840 | 0.3062 | 0.3032 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 32 | 0.6198 | 0.7485 |
| seed_p | 32 | -0.4711 | -0.3923 |
| seed_p_vs_seed_pars | 27 | -0.6603 | -0.7207 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
