# YBR003W
Status: ok. Length: 1575 nt. Measured usable bases: 788.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 788 | 0.3064 | 0.3089 |
| rnafold | ok | 788 | 0.2810 | 0.2693 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 120 | 0.0413 | -0.0955 |
| seed_p | 120 | -0.1635 | -0.4046 |
| seed_p_vs_seed_pars | 80 | 0.2896 | 0.2070 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
