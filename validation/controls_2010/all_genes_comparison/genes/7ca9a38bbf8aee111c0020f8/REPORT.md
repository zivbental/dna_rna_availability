# YPL053C
Status: ok. Length: 1514 nt. Measured usable bases: 750. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 750 | 0.3600 | 0.3478 |
| rnafold | ok | 750 | 0.3318 | 0.3143 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 149 | -0.3760 | -0.3879 |
| seed_p | 149 | -0.5436 | -0.4022 |
| seed_p_vs_seed_pars | 102 | -0.6870 | -0.4160 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
