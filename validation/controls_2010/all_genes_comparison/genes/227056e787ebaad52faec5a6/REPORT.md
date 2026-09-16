# YIL118W
Status: ok. Length: 958 nt. Measured usable bases: 539. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 539 | 0.4058 | 0.3794 |
| rnafold | ok | 539 | 0.3704 | 0.3558 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 269 | -0.2594 | -0.2353 |
| seed_p | 269 | -0.3097 | -0.2924 |
| seed_p_vs_seed_pars | 223 | -0.3232 | -0.1838 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
