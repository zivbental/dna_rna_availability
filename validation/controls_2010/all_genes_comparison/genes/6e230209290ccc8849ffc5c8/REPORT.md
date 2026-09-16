# YER083C
Status: ok. Length: 902 nt. Measured usable bases: 652. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 652 | 0.2449 | 0.2303 |
| rnafold | ok | 652 | 0.2224 | 0.2108 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 461 | -0.2595 | -0.5237 |
| seed_p | 461 | -0.2653 | -0.3062 |
| seed_p_vs_seed_pars | 358 | -0.1627 | -0.2598 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
