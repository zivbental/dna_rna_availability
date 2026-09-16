# YJR072C
Status: ok. Length: 1221 nt. Measured usable bases: 864. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 864 | 0.3603 | 0.3452 |
| rnafold | ok | 864 | 0.3591 | 0.3549 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 483 | 0.0062 | -0.2271 |
| seed_p | 483 | -0.1933 | -0.2130 |
| seed_p_vs_seed_pars | 358 | -0.1855 | -0.2859 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
