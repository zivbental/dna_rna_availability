# YGL089C
Status: ok. Length: 363 nt. Measured usable bases: 323. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 323 | 0.3458 | 0.3533 |
| rnafold | ok | 323 | 0.3166 | 0.3335 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 306 | -0.1221 | -0.2347 |
| seed_p | 306 | -0.1262 | -0.1947 |
| seed_p_vs_seed_pars | 304 | -0.2455 | -0.3045 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
