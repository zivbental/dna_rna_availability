# YMR195W
Status: ok. Length: 589 nt. Measured usable bases: 294. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 294 | 0.4159 | 0.4424 |
| rnafold | ok | 294 | 0.3437 | 0.3787 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 73 | -0.1063 | 0.0850 |
| seed_p | 73 | -0.0711 | 0.1195 |
| seed_p_vs_seed_pars | 59 | 0.0055 | 0.1256 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
