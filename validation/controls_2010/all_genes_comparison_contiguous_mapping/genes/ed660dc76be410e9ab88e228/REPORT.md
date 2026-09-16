# YBR080C
Status: ok. Length: 2420 nt. Measured usable bases: 1287.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1287 | 0.3150 | 0.2968 |
| rnafold | ok | 1287 | 0.2256 | 0.2269 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 299 | -0.3508 | -0.0046 |
| seed_p | 299 | -0.4136 | -0.2283 |
| seed_p_vs_seed_pars | 234 | -0.6208 | -0.3671 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
