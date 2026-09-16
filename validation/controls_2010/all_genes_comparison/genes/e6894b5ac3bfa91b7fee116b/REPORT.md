# YLL014W
Status: ok. Length: 515 nt. Measured usable bases: 315. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 315 | 0.2927 | 0.2967 |
| rnafold | ok | 315 | 0.3651 | 0.3417 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 257 | -0.1455 | -0.2759 |
| seed_p | 257 | -0.4886 | -0.4476 |
| seed_p_vs_seed_pars | 216 | -0.7091 | -0.5524 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
