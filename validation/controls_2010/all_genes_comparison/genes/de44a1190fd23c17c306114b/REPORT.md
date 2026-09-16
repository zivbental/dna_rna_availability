# YNL048W
Status: ok. Length: 1757 nt. Measured usable bases: 807. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 807 | 0.2892 | 0.2774 |
| rnafold | ok | 807 | 0.2290 | 0.2064 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 109 | -0.2262 | -0.2575 |
| seed_p | 109 | -0.5005 | -0.4692 |
| seed_p_vs_seed_pars | 88 | -0.6687 | -0.4218 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
