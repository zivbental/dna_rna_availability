# YOR298C-A
Status: ok. Length: 709 nt. Measured usable bases: 557. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 557 | 0.4072 | 0.3862 |
| rnafold | ok | 557 | 0.3064 | 0.3020 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 479 | -0.0885 | -0.0941 |
| seed_p | 479 | -0.2114 | -0.2083 |
| seed_p_vs_seed_pars | 428 | -0.5090 | -0.4171 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
