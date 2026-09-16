# YBL047C
Status: ok. Length: 4513 nt. Measured usable bases: 2700. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2700 | 0.2876 | 0.2782 |
| rnafold | ok | 2700 | 0.2552 | 0.2459 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 955 | -0.1706 | -0.2734 |
| seed_p | 955 | -0.3600 | -0.3524 |
| seed_p_vs_seed_pars | 724 | -0.3540 | -0.3474 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
