# YKR003W
Status: ok. Length: 1475 nt. Measured usable bases: 658. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 658 | 0.3276 | 0.3221 |
| rnafold | ok | 658 | 0.2815 | 0.2756 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 62 | 0.0715 | -0.0407 |
| seed_p | 62 | 0.3057 | 0.2370 |
| seed_p_vs_seed_pars | 49 | 0.3903 | 0.2136 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
