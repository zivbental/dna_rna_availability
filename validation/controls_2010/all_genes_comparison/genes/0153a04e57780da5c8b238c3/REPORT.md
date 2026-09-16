# YNL217W
Status: ok. Length: 1115 nt. Measured usable bases: 709. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 709 | 0.2959 | 0.2982 |
| rnafold | ok | 709 | 0.2704 | 0.2842 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 398 | 0.1773 | -0.1470 |
| seed_p | 398 | -0.0248 | -0.0805 |
| seed_p_vs_seed_pars | 315 | -0.2199 | -0.3120 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
