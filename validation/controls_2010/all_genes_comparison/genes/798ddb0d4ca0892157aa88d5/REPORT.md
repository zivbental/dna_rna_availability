# YOR101W
Status: ok. Length: 1227 nt. Measured usable bases: 710. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 710 | 0.3526 | 0.3186 |
| rnafold | ok | 710 | 0.3263 | 0.3353 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 248 | -0.0265 | -0.0251 |
| seed_p | 248 | -0.2769 | -0.2264 |
| seed_p_vs_seed_pars | 179 | -0.4753 | -0.4104 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
