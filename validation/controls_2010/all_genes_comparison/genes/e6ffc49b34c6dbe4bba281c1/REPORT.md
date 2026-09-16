# YMR012W
Status: ok. Length: 4096 nt. Measured usable bases: 2486. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2486 | 0.2655 | 0.2486 |
| rnafold | ok | 2486 | 0.2464 | 0.2314 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 950 | -0.0220 | -0.1601 |
| seed_p | 950 | -0.3142 | -0.3601 |
| seed_p_vs_seed_pars | 678 | -0.4052 | -0.4488 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
