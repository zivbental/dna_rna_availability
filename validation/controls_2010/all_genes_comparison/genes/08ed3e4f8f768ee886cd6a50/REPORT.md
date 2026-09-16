# YKR018C
Status: ok. Length: 2357 nt. Measured usable bases: 1382. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1382 | 0.3355 | 0.3316 |
| rnafold | ok | 1382 | 0.2505 | 0.2619 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 381 | -0.1465 | -0.2953 |
| seed_p | 381 | -0.2006 | -0.1843 |
| seed_p_vs_seed_pars | 276 | -0.4008 | -0.2708 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
