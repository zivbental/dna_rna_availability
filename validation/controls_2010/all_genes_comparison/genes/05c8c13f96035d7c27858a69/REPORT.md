# YOR125C
Status: ok. Length: 867 nt. Measured usable bases: 461. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 461 | 0.3488 | 0.3624 |
| rnafold | ok | 461 | 0.2730 | 0.3246 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 101 | -0.3566 | -0.1887 |
| seed_p | 101 | -0.4207 | -0.4005 |
| seed_p_vs_seed_pars | 63 | 0.3181 | 0.4053 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
