# YNL090W
Status: ok. Length: 843 nt. Measured usable bases: 463. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 463 | 0.2857 | 0.2753 |
| rnafold | ok | 463 | 0.3007 | 0.2829 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 86 | -0.0931 | -0.4546 |
| seed_p | 86 | -0.3729 | -0.3964 |
| seed_p_vs_seed_pars | 58 | -0.4651 | -0.4833 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
