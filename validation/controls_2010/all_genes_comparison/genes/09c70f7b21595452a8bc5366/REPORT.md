# YKR007W
Status: ok. Length: 646 nt. Measured usable bases: 300. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 300 | 0.4558 | 0.4613 |
| rnafold | ok | 300 | 0.3139 | 0.3381 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 118 | 0.1789 | 0.3837 |
| seed_p | 118 | -0.2159 | 0.0981 |
| seed_p_vs_seed_pars | 92 | -0.2739 | -0.1000 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
