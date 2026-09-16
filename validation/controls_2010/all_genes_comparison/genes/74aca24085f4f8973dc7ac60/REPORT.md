# YNL289W
Status: ok. Length: 1069 nt. Measured usable bases: 436. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 436 | 0.3350 | 0.3358 |
| rnafold | ok | 436 | 0.2757 | 0.2884 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 31 | -0.0481 | -0.5987 |
| seed_p | 31 | 0.0322 | 0.1533 |
| seed_p_vs_seed_pars | 22 | -0.0184 | 0.1441 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
