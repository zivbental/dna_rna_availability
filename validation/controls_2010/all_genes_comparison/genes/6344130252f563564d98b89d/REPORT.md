# YDL063C
Status: ok. Length: 2144 nt. Measured usable bases: 990. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 990 | 0.2917 | 0.2841 |
| rnafold | ok | 990 | 0.2573 | 0.2636 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 94 | -0.0125 | -0.2070 |
| seed_p | 94 | -0.2066 | -0.2631 |
| seed_p_vs_seed_pars | 64 | -0.7592 | -0.6916 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
