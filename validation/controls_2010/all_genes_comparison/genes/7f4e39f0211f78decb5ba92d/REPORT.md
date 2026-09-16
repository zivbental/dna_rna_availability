# YOR142W
Status: ok. Length: 1385 nt. Measured usable bases: 1022. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1022 | 0.2584 | 0.2518 |
| rnafold | ok | 1022 | 0.2358 | 0.2273 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 702 | -0.1324 | -0.1792 |
| seed_p | 702 | -0.2294 | -0.1775 |
| seed_p_vs_seed_pars | 552 | -0.4121 | -0.3828 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
