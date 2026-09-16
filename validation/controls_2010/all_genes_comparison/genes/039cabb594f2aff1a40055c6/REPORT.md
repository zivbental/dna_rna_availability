# YIL117C
Status: ok. Length: 1136 nt. Measured usable bases: 511. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 511 | 0.3096 | 0.3039 |
| rnafold | ok | 511 | 0.3289 | 0.3242 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 99 | 0.2110 | 0.1952 |
| seed_p | 99 | 0.0366 | -0.0426 |
| seed_p_vs_seed_pars | 59 | -0.1367 | 0.0433 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
