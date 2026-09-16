# YMR310C
Status: ok. Length: 1043 nt. Measured usable bases: 597. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 597 | 0.2823 | 0.2789 |
| rnafold | ok | 597 | 0.2808 | 0.2772 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 99 | -0.2277 | -0.5545 |
| seed_p | 99 | -0.4883 | -0.5624 |
| seed_p_vs_seed_pars | 88 | -0.6453 | -0.6025 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
