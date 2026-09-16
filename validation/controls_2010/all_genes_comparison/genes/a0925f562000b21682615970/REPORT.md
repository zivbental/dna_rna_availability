# YIL021W
Status: ok. Length: 1154 nt. Measured usable bases: 590. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 590 | 0.3848 | 0.3762 |
| rnafold | ok | 590 | 0.3283 | 0.3397 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 205 | -0.2260 | -0.4135 |
| seed_p | 205 | -0.2845 | -0.4330 |
| seed_p_vs_seed_pars | 150 | -0.1486 | -0.3108 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
