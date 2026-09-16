# YHR192W
Status: ok. Length: 941 nt. Measured usable bases: 436. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 436 | 0.2891 | 0.2947 |
| rnafold | ok | 436 | 0.2473 | 0.2486 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 63 | -0.5008 | -0.8243 |
| seed_p | 63 | -0.4649 | -0.5939 |
| seed_p_vs_seed_pars | 51 | -0.1300 | -0.4614 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
