# YJL178C
Status: ok. Length: 937 nt. Measured usable bases: 626. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 626 | 0.4011 | 0.3976 |
| rnafold | ok | 626 | 0.3771 | 0.3656 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 393 | -0.1579 | -0.3809 |
| seed_p | 393 | -0.3015 | -0.3449 |
| seed_p_vs_seed_pars | 313 | -0.3208 | -0.3293 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
