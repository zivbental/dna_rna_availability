# YOR171C
Status: ok. Length: 2105 nt. Measured usable bases: 957. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 957 | 0.3507 | 0.3412 |
| rnafold | ok | 957 | 0.2990 | 0.2980 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 87 | 0.0951 | 0.2457 |
| seed_p | 87 | 0.2584 | 0.1371 |
| seed_p_vs_seed_pars | 60 | -0.0976 | -0.1295 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
