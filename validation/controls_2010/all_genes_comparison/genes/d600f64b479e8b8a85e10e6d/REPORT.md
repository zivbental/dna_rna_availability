# YDR033W
Status: ok. Length: 1643 nt. Measured usable bases: 1450. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1450 | 0.3144 | 0.3151 |
| rnafold | ok | 1450 | 0.2468 | 0.2451 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1395 | -0.0700 | -0.2954 |
| seed_p | 1395 | -0.3248 | -0.3424 |
| seed_p_vs_seed_pars | 1250 | -0.2920 | -0.3252 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
