# YLR304C
Status: ok. Length: 2651 nt. Measured usable bases: 2232. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2232 | 0.3515 | 0.3379 |
| rnafold | ok | 2232 | 0.3041 | 0.3038 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 2105 | -0.1701 | -0.1170 |
| seed_p | 2105 | -0.2132 | -0.1560 |
| seed_p_vs_seed_pars | 1768 | -0.3548 | -0.2729 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
