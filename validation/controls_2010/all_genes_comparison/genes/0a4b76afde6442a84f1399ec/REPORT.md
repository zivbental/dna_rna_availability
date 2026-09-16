# YOR382W
Status: ok. Length: 598 nt. Measured usable bases: 342. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 342 | 0.2968 | 0.2823 |
| rnafold | ok | 342 | 0.2347 | 0.2614 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 130 | -0.5250 | -0.3788 |
| seed_p | 130 | -0.1921 | -0.1107 |
| seed_p_vs_seed_pars | 73 | -0.0400 | 0.0015 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
