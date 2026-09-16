# YML059C
Status: ok. Length: 5260 nt. Measured usable bases: 2300. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2300 | 0.2348 | 0.2254 |
| rnafold | ok | 2300 | 0.2236 | 0.2257 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 222 | 0.2355 | -0.2688 |
| seed_p | 222 | 0.0096 | -0.1702 |
| seed_p_vs_seed_pars | 134 | 0.2419 | 0.0050 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
