# YFR021W
Status: ok. Length: 1680 nt. Measured usable bases: 752. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 752 | 0.3261 | 0.3135 |
| rnafold | ok | 752 | 0.2650 | 0.2554 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 176 | -0.4785 | -0.6980 |
| seed_p | 176 | -0.6599 | -0.7203 |
| seed_p_vs_seed_pars | 144 | -0.7301 | -0.7782 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
