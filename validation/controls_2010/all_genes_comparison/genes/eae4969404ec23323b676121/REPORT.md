# YFL044C
Status: ok. Length: 1118 nt. Measured usable bases: 576. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 576 | 0.3091 | 0.2971 |
| rnafold | ok | 576 | 0.3258 | 0.3290 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 159 | -0.0038 | -0.1498 |
| seed_p | 159 | 0.1543 | 0.1501 |
| seed_p_vs_seed_pars | 88 | -0.0478 | -0.2673 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
