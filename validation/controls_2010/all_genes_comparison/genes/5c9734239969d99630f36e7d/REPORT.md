# YLR002C
Status: ok. Length: 2092 nt. Measured usable bases: 843. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 843 | 0.3095 | 0.3214 |
| rnafold | ok | 843 | 0.2943 | 0.3124 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 66 | -0.0976 | -0.3137 |
| seed_p | 66 | 0.0029 | -0.1447 |
| seed_p_vs_seed_pars | 35 | 0.0557 | 0.0132 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
