# YPL263C
Status: ok. Length: 2094 nt. Measured usable bases: 1067. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1067 | 0.3227 | 0.3078 |
| rnafold | ok | 1067 | 0.3443 | 0.3334 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 270 | 0.0800 | 0.2631 |
| seed_p | 270 | 0.0263 | 0.0887 |
| seed_p_vs_seed_pars | 242 | -0.1064 | 0.0519 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
