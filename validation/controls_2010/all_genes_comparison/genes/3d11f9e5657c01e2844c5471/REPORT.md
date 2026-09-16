# YKR025W
Status: ok. Length: 989 nt. Measured usable bases: 464. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 464 | 0.3673 | 0.3731 |
| rnafold | ok | 464 | 0.3333 | 0.3473 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 112 | -0.0351 | 0.0066 |
| seed_p | 112 | -0.1287 | -0.3808 |
| seed_p_vs_seed_pars | 69 | -0.2340 | -0.4007 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
