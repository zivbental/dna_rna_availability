# YDL226C
Status: ok. Length: 1156 nt. Measured usable bases: 729. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 729 | 0.3848 | 0.3752 |
| rnafold | ok | 729 | 0.3607 | 0.3433 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 280 | -0.0575 | -0.2462 |
| seed_p | 280 | -0.3349 | -0.3967 |
| seed_p_vs_seed_pars | 201 | -0.5315 | -0.4235 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
