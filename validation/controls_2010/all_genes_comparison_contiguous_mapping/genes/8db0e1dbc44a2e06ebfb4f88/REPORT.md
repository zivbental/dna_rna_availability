# YBR058C-A
Status: ok. Length: 396 nt. Measured usable bases: 241.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 241 | 0.2747 | 0.2762 |
| rnafold | ok | 241 | 0.1752 | 0.2352 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 132 | -0.1065 | -0.2427 |
| seed_p | 132 | -0.7557 | -0.6677 |
| seed_p_vs_seed_pars | 118 | -0.9030 | -0.6513 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
