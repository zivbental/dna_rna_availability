# YIL044C
Status: ok. Length: 1031 nt. Measured usable bases: 461. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 461 | 0.3398 | 0.3333 |
| rnafold | ok | 461 | 0.2685 | 0.2661 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 66 | -0.5749 | -0.2791 |
| seed_p | 66 | -0.7055 | -0.6158 |
| seed_p_vs_seed_pars | 48 | -0.3856 | -0.2908 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
