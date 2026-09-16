# YKR074W
Status: ok. Length: 625 nt. Measured usable bases: 393. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 393 | 0.3507 | 0.3370 |
| rnafold | ok | 393 | 0.1959 | 0.1940 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 246 | 0.1332 | -0.2305 |
| seed_p | 246 | -0.3366 | -0.3162 |
| seed_p_vs_seed_pars | 214 | -0.3261 | -0.3226 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
