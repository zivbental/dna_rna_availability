# YOR153W
Status: ok. Length: 4783 nt. Measured usable bases: 4286. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 4286 | 0.2909 | 0.2773 |
| rnafold | ok | 4286 | 0.2317 | 0.2172 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 4141 | -0.1022 | -0.0436 |
| seed_p | 4141 | -0.1707 | -0.1335 |
| seed_p_vs_seed_pars | 3682 | -0.3183 | -0.2697 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
