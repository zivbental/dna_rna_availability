# YDR262W
Status: ok. Length: 1055 nt. Measured usable bases: 509. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 509 | 0.2793 | 0.2903 |
| rnafold | ok | 509 | 0.2150 | 0.2158 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 129 | -0.2214 | -0.0567 |
| seed_p | 129 | 0.1457 | 0.1437 |
| seed_p_vs_seed_pars | 94 | 0.3156 | 0.0677 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
