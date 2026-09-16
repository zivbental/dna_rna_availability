# YKL096W-A
Status: ok. Length: 500 nt. Measured usable bases: 414. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 414 | 0.2534 | 0.2456 |
| rnafold | ok | 414 | 0.2104 | 0.1731 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 360 | -0.0836 | -0.3445 |
| seed_p | 360 | -0.3930 | -0.3685 |
| seed_p_vs_seed_pars | 337 | -0.3867 | -0.3335 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
