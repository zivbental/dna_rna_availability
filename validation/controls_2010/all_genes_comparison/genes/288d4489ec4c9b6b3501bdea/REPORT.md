# YHR049W
Status: ok. Length: 892 nt. Measured usable bases: 655. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 655 | 0.2571 | 0.2405 |
| rnafold | ok | 655 | 0.1942 | 0.2081 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 522 | -0.1994 | -0.2387 |
| seed_p | 522 | -0.1728 | -0.1250 |
| seed_p_vs_seed_pars | 467 | -0.2191 | -0.1332 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
