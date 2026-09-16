# YDR297W
Status: ok. Length: 1274 nt. Measured usable bases: 1003. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1003 | 0.3049 | 0.2892 |
| rnafold | ok | 1003 | 0.2271 | 0.2202 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 782 | -0.0676 | -0.0483 |
| seed_p | 782 | 0.0130 | -0.0523 |
| seed_p_vs_seed_pars | 656 | -0.0276 | -0.0521 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
