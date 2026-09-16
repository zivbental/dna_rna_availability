# YOR048C
Status: ok. Length: 3121 nt. Measured usable bases: 1429. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1429 | 0.3486 | 0.3305 |
| rnafold | ok | 1429 | 0.2535 | 0.2488 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 328 | 0.0684 | -0.0832 |
| seed_p | 328 | -0.1213 | -0.1443 |
| seed_p_vs_seed_pars | 247 | 0.0358 | 0.1214 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
