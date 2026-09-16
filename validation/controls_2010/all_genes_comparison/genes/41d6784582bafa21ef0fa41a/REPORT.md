# YKR038C
Status: ok. Length: 1574 nt. Measured usable bases: 953. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 953 | 0.3913 | 0.3867 |
| rnafold | ok | 953 | 0.3584 | 0.3794 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 558 | -0.1550 | -0.1858 |
| seed_p | 558 | -0.2867 | -0.2313 |
| seed_p_vs_seed_pars | 409 | -0.3991 | -0.3419 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
