# YPL105C
Status: ok. Length: 2673 nt. Measured usable bases: 1042. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1042 | 0.3467 | 0.3425 |
| rnafold | ok | 1042 | 0.3111 | 0.3013 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 80 | -0.0966 | 0.2249 |
| seed_p | 80 | -0.2892 | -0.0761 |
| seed_p_vs_seed_pars | 64 | -0.1611 | 0.0659 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
