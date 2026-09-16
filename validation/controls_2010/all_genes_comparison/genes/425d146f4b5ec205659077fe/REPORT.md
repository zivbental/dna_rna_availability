# YDL051W
Status: ok. Length: 961 nt. Measured usable bases: 703. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 703 | 0.3529 | 0.3565 |
| rnafold | ok | 703 | 0.3082 | 0.3081 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 450 | -0.2008 | -0.2653 |
| seed_p | 450 | -0.2155 | -0.1883 |
| seed_p_vs_seed_pars | 329 | -0.1708 | -0.2418 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
