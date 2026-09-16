# YLL018C
Status: ok. Length: 1831 nt. Measured usable bases: 1466. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1466 | 0.3497 | 0.3310 |
| rnafold | ok | 1466 | 0.3161 | 0.3039 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1242 | 0.0188 | 0.0658 |
| seed_p | 1242 | 0.0015 | 0.0423 |
| seed_p_vs_seed_pars | 1110 | -0.2787 | -0.2294 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
