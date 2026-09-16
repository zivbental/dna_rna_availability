# YMR189W
Status: ok. Length: 3342 nt. Measured usable bases: 1782. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1782 | 0.2685 | 0.2455 |
| rnafold | ok | 1782 | 0.2384 | 0.2201 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 428 | 0.0089 | -0.0432 |
| seed_p | 428 | -0.0885 | -0.1162 |
| seed_p_vs_seed_pars | 290 | -0.1823 | -0.0370 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
