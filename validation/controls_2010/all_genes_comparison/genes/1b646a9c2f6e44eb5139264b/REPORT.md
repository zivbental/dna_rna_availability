# YGR189C
Status: ok. Length: 1653 nt. Measured usable bases: 1315. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1315 | 0.2349 | 0.2312 |
| rnafold | ok | 1315 | 0.1493 | 0.1511 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1081 | -0.1669 | -0.1290 |
| seed_p | 1081 | -0.3964 | -0.3494 |
| seed_p_vs_seed_pars | 969 | -0.4138 | -0.3707 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
