# YOR099W
Status: ok. Length: 1339 nt. Measured usable bases: 1088. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1088 | 0.3119 | 0.2887 |
| rnafold | ok | 1088 | 0.2496 | 0.2521 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 946 | -0.0099 | -0.0178 |
| seed_p | 946 | -0.1052 | -0.0531 |
| seed_p_vs_seed_pars | 847 | -0.2370 | -0.1421 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
