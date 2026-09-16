# YEL046C
Status: ok. Length: 1728 nt. Measured usable bases: 1447. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1447 | 0.3819 | 0.3629 |
| rnafold | ok | 1447 | 0.3111 | 0.3043 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1319 | -0.0860 | -0.2114 |
| seed_p | 1319 | -0.2574 | -0.2453 |
| seed_p_vs_seed_pars | 1208 | -0.3732 | -0.3761 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
