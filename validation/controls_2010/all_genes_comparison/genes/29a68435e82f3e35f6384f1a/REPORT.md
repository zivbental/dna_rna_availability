# YOL155C
Status: ok. Length: 2904 nt. Measured usable bases: 943. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 943 | 0.2945 | 0.2796 |
| rnafold | ok | 943 | 0.2547 | 0.2455 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 57 | 0.0046 | -0.1112 |
| seed_p | 57 | -0.3075 | -0.3186 |
| seed_p_vs_seed_pars | 54 | -0.3767 | -0.4192 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
