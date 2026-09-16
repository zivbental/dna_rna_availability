# YOL004W
Status: ok. Length: 4932 nt. Measured usable bases: 1877. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1877 | 0.3167 | 0.3046 |
| rnafold | ok | 1877 | 0.2872 | 0.2696 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 176 | -0.0066 | -0.0081 |
| seed_p | 176 | 0.0245 | 0.0478 |
| seed_p_vs_seed_pars | 117 | -0.0503 | -0.0763 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
