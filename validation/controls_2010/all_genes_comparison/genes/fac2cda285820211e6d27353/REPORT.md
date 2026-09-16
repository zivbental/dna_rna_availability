# YIL142W
Status: ok. Length: 1638 nt. Measured usable bases: 1298. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1298 | 0.3865 | 0.3821 |
| rnafold | ok | 1298 | 0.3683 | 0.3525 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1047 | -0.0515 | -0.1394 |
| seed_p | 1047 | -0.2869 | -0.2399 |
| seed_p_vs_seed_pars | 851 | -0.4068 | -0.3677 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
