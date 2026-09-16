# YOR051C
Status: ok. Length: 1437 nt. Measured usable bases: 800. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 800 | 0.3897 | 0.3859 |
| rnafold | ok | 800 | 0.3394 | 0.3366 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 315 | 0.1075 | -0.0557 |
| seed_p | 315 | -0.0404 | 0.0116 |
| seed_p_vs_seed_pars | 183 | 0.0178 | 0.0651 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
