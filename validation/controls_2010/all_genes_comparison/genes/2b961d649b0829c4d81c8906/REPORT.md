# YNL287W
Status: ok. Length: 3234 nt. Measured usable bases: 2183. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 2183 | 0.2473 | 0.2399 |
| rnafold | ok | 2183 | 0.2375 | 0.2314 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1093 | -0.0353 | 0.0434 |
| seed_p | 1093 | -0.0879 | -0.0306 |
| seed_p_vs_seed_pars | 836 | -0.1254 | -0.1006 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
