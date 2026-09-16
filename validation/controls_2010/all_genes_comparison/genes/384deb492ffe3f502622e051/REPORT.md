# YOR063W
Status: ok. Length: 1308 nt. Measured usable bases: 1239. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1239 | 0.3995 | 0.3755 |
| rnafold | ok | 1239 | 0.3016 | 0.2816 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1205 | -0.0535 | -0.1136 |
| seed_p | 1205 | -0.2432 | -0.1505 |
| seed_p_vs_seed_pars | 1193 | -0.3681 | -0.2877 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
