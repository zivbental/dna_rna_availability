# YDR051C
Status: ok. Length: 1078 nt. Measured usable bases: 391. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 391 | 0.4356 | 0.4011 |
| rnafold | ok | 391 | 0.3797 | 0.3541 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 44 | -0.2315 | -0.1730 |
| seed_p | 44 | -0.5701 | -0.4387 |
| seed_p_vs_seed_pars | 44 | -0.6151 | -0.4419 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
