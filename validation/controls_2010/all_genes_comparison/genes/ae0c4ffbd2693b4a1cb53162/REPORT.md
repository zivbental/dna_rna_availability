# YOR222W
Status: ok. Length: 1434 nt. Measured usable bases: 781. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 781 | 0.3180 | 0.3198 |
| rnafold | ok | 781 | 0.2916 | 0.2964 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 287 | -0.0100 | 0.0376 |
| seed_p | 287 | -0.2109 | -0.2507 |
| seed_p_vs_seed_pars | 190 | 0.0264 | -0.1121 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
