# YGL210W
Status: ok. Length: 801 nt. Measured usable bases: 369. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 369 | 0.3505 | 0.3298 |
| rnafold | ok | 369 | 0.3136 | 0.3005 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 77 | -0.3306 | -0.5316 |
| seed_p | 77 | -0.2064 | -0.2050 |
| seed_p_vs_seed_pars | 76 | -0.2480 | -0.1607 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
