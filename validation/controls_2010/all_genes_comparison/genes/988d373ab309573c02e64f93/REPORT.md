# YKR065C
Status: ok. Length: 702 nt. Measured usable bases: 462. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 462 | 0.2893 | 0.2643 |
| rnafold | ok | 462 | 0.2741 | 0.2426 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 229 | -0.1525 | 0.1365 |
| seed_p | 229 | -0.1740 | -0.0927 |
| seed_p_vs_seed_pars | 156 | -0.4360 | -0.2870 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
