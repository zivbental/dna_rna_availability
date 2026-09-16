# YPL149W
Status: ok. Length: 1028 nt. Measured usable bases: 486. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 486 | 0.2972 | 0.2708 |
| rnafold | ok | 486 | 0.2987 | 0.2667 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 61 | 0.5424 | 0.5676 |
| seed_p | 61 | 0.3483 | 0.2921 |
| seed_p_vs_seed_pars | 44 | -0.1200 | -0.2214 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
