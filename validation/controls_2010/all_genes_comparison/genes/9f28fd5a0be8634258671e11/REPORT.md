# YHR027C
Status: ok. Length: 3262 nt. Measured usable bases: 2061. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2061 | 0.2809 | 0.2763 |
| rnafold | ok | 2061 | 0.2506 | 0.2392 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1042 | 0.0170 | 0.0068 |
| seed_p | 1042 | -0.2763 | -0.2529 |
| seed_p_vs_seed_pars | 791 | -0.3413 | -0.3707 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
