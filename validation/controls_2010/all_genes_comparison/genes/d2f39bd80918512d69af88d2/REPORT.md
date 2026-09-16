# YHR008C
Status: ok. Length: 895 nt. Measured usable bases: 670. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 670 | 0.3767 | 0.3604 |
| rnafold | ok | 670 | 0.3876 | 0.3745 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 532 | -0.3618 | -0.5857 |
| seed_p | 532 | -0.6283 | -0.6455 |
| seed_p_vs_seed_pars | 419 | -0.6178 | -0.6404 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
