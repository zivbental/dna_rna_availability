# YOR283W
Status: ok. Length: 921 nt. Measured usable bases: 445. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 445 | 0.2014 | 0.2055 |
| rnafold | ok | 445 | 0.1905 | 0.2119 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 96 | -0.0201 | -0.1298 |
| seed_p | 96 | 0.1053 | 0.1820 |
| seed_p_vs_seed_pars | 60 | 0.0535 | 0.1585 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
