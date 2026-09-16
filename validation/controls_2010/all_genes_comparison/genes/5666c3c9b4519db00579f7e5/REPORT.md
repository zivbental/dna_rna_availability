# YOR164C
Status: ok. Length: 1074 nt. Measured usable bases: 717. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 717 | 0.2431 | 0.2318 |
| rnafold | ok | 717 | 0.2083 | 0.2083 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 469 | 0.1132 | 0.0927 |
| seed_p | 469 | -0.2240 | -0.1463 |
| seed_p_vs_seed_pars | 420 | -0.1970 | -0.1696 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
