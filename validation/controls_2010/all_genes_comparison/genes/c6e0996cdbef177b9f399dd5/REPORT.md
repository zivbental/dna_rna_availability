# YDR472W
Status: ok. Length: 1360 nt. Measured usable bases: 602. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 602 | 0.2844 | 0.2636 |
| rnafold | ok | 602 | 0.2236 | 0.2203 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 121 | -0.4854 | -0.3835 |
| seed_p | 121 | -0.3355 | -0.3025 |
| seed_p_vs_seed_pars | 71 | -0.3379 | -0.4466 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
