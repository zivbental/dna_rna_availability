# YGR173W
Status: ok. Length: 1366 nt. Measured usable bases: 710. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 710 | 0.3488 | 0.3569 |
| rnafold | ok | 710 | 0.3168 | 0.3371 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 121 | -0.3372 | -0.4028 |
| seed_p | 121 | -0.2403 | -0.2038 |
| seed_p_vs_seed_pars | 57 | -0.2701 | -0.3000 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
