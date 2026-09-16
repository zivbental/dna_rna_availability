# YNL087W
Status: ok. Length: 3903 nt. Measured usable bases: 2251. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2251 | 0.3460 | 0.3379 |
| rnafold | ok | 2251 | 0.2790 | 0.2800 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 681 | 0.0285 | 0.1592 |
| seed_p | 681 | -0.0619 | 0.0180 |
| seed_p_vs_seed_pars | 523 | -0.1454 | 0.0042 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
