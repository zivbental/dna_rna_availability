# YHR017W
Status: ok. Length: 1261 nt. Measured usable bases: 511. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 511 | 0.2570 | 0.2487 |
| rnafold | ok | 511 | 0.2350 | 0.2258 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 60 | -0.2872 | -0.1483 |
| seed_p | 60 | -0.2316 | -0.1664 |
| seed_p_vs_seed_pars | 53 | -0.5749 | -0.6451 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
