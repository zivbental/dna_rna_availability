# YDL141W
Status: ok. Length: 2522 nt. Measured usable bases: 1168. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1168 | 0.3030 | 0.2935 |
| rnafold | ok | 1168 | 0.2751 | 0.2564 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 203 | -0.2848 | -0.4537 |
| seed_p | 203 | -0.0832 | -0.2799 |
| seed_p_vs_seed_pars | 169 | -0.2055 | -0.3217 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
