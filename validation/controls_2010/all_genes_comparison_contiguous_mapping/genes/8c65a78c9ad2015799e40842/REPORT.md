# YBR041W
Status: ok. Length: 2240 nt. Measured usable bases: 1308.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1308 | 0.3535 | 0.3337 |
| rnafold | ok | 1308 | 0.2259 | 0.2344 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 470 | -0.2909 | -0.1284 |
| seed_p | 470 | -0.2861 | -0.3081 |
| seed_p_vs_seed_pars | 354 | -0.5189 | -0.4643 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
