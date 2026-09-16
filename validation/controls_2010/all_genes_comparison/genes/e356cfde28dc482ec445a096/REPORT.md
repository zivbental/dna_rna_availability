# YKL142W
Status: ok. Length: 849 nt. Measured usable bases: 454. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 454 | 0.4098 | 0.3996 |
| rnafold | ok | 454 | 0.3248 | 0.3411 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 176 | -0.1986 | -0.0383 |
| seed_p | 176 | -0.2689 | -0.0411 |
| seed_p_vs_seed_pars | 135 | -0.2885 | -0.2301 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
