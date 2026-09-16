# YGR152C
Status: ok. Length: 940 nt. Measured usable bases: 394. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 394 | 0.3144 | 0.3114 |
| rnafold | ok | 394 | 0.3147 | 0.3114 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 50 | -0.1456 | -0.1792 |
| seed_p | 50 | 0.1288 | 0.4231 |
| seed_p_vs_seed_pars | 47 | -0.2054 | 0.2652 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
