# YJR068W
Status: ok. Length: 1326 nt. Measured usable bases: 601. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 601 | 0.3640 | 0.3605 |
| rnafold | ok | 601 | 0.3249 | 0.3229 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 138 | -0.3608 | -0.4902 |
| seed_p | 138 | -0.1802 | -0.1536 |
| seed_p_vs_seed_pars | 93 | -0.5054 | -0.6958 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
