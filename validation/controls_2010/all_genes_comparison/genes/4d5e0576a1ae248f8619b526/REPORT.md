# YML051W
Status: ok. Length: 1465 nt. Measured usable bases: 975. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 975 | 0.2385 | 0.2299 |
| rnafold | ok | 975 | 0.1777 | 0.1721 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 486 | 0.0370 | -0.0099 |
| seed_p | 486 | -0.1998 | -0.1050 |
| seed_p_vs_seed_pars | 386 | -0.2124 | -0.1184 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
