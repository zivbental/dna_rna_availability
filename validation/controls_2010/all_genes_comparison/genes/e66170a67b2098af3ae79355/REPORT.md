# YGR195W
Status: ok. Length: 923 nt. Measured usable bases: 584. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 584 | 0.2681 | 0.2602 |
| rnafold | ok | 584 | 0.1906 | 0.1976 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 261 | 0.1004 | -0.0648 |
| seed_p | 261 | -0.2312 | -0.2894 |
| seed_p_vs_seed_pars | 170 | -0.3150 | -0.3368 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
