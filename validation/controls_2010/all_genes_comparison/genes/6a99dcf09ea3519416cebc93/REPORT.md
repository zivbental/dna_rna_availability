# YIL036W
Status: ok. Length: 1926 nt. Measured usable bases: 718. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 718 | 0.3483 | 0.3372 |
| rnafold | ok | 718 | 0.3032 | 0.3032 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 70 | -0.3729 | -0.6485 |
| seed_p | 70 | -0.2623 | -0.4042 |
| seed_p_vs_seed_pars | 54 | -0.0295 | -0.1577 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
