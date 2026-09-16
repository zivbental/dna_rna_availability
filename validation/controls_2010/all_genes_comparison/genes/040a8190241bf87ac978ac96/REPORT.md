# YJL157C
Status: ok. Length: 2628 nt. Measured usable bases: 1414. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1414 | 0.3779 | 0.3623 |
| rnafold | ok | 1414 | 0.3170 | 0.3175 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 402 | -0.4015 | -0.3666 |
| seed_p | 402 | -0.4626 | -0.2668 |
| seed_p_vs_seed_pars | 341 | -0.4759 | -0.3304 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
