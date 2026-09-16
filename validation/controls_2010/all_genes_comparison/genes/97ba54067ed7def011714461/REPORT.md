# YOR321W
Status: ok. Length: 2339 nt. Measured usable bases: 1140. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1140 | 0.3004 | 0.2753 |
| rnafold | ok | 1140 | 0.2649 | 0.2457 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 191 | 0.0194 | 0.0384 |
| seed_p | 191 | -0.1481 | -0.0142 |
| seed_p_vs_seed_pars | 140 | -0.3024 | 0.1201 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
