# YHR170W
Status: ok. Length: 1710 nt. Measured usable bases: 1220. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1220 | 0.3529 | 0.3451 |
| rnafold | ok | 1220 | 0.3056 | 0.2985 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 719 | 0.0780 | 0.0333 |
| seed_p | 719 | -0.1021 | -0.0940 |
| seed_p_vs_seed_pars | 576 | -0.2881 | -0.2555 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
