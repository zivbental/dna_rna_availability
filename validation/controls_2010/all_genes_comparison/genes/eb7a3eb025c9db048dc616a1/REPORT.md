# YCR011C
Status: ok. Length: 3340 nt. Measured usable bases: 1888. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1888 | 0.2879 | 0.2757 |
| rnafold | ok | 1888 | 0.2294 | 0.2132 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 434 | -0.1358 | -0.0371 |
| seed_p | 434 | -0.1142 | -0.0829 |
| seed_p_vs_seed_pars | 329 | -0.1651 | -0.1414 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
