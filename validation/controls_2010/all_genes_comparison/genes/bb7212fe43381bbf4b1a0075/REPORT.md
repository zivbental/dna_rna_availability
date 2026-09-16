# YLR201C
Status: ok. Length: 910 nt. Measured usable bases: 379. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 379 | 0.3353 | 0.3109 |
| rnafold | ok | 379 | 0.3210 | 0.2899 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 30 | -0.0967 | -0.5791 |
| seed_p | 30 | -0.5979 | -0.5743 |
| seed_p_vs_seed_pars | 25 | -0.8090 | -0.8713 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
