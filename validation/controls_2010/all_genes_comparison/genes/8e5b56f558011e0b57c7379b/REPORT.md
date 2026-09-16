# YKL001C
Status: ok. Length: 690 nt. Measured usable bases: 345. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 345 | 0.3722 | 0.3356 |
| rnafold | ok | 345 | 0.2941 | 0.2947 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 93 | -0.2579 | -0.3731 |
| seed_p | 93 | -0.0050 | -0.0056 |
| seed_p_vs_seed_pars | 84 | -0.0016 | 0.0004 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
