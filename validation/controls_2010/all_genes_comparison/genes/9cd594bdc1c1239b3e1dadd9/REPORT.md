# YGR233C
Status: ok. Length: 3671 nt. Measured usable bases: 1340. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1340 | 0.2767 | 0.2700 |
| rnafold | ok | 1340 | 0.2551 | 0.2464 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 154 | -0.0144 | -0.2995 |
| seed_p | 154 | -0.2549 | -0.3542 |
| seed_p_vs_seed_pars | 122 | -0.4720 | -0.5088 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
