# YDR236C
Status: ok. Length: 761 nt. Measured usable bases: 440. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 440 | 0.3594 | 0.3175 |
| rnafold | ok | 440 | 0.3224 | 0.2691 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 135 | -0.1527 | 0.0991 |
| seed_p | 135 | -0.3348 | -0.1650 |
| seed_p_vs_seed_pars | 102 | -0.6037 | -0.1614 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
