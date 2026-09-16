# YML092C
Status: ok. Length: 854 nt. Measured usable bases: 661. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 661 | 0.3548 | 0.3349 |
| rnafold | ok | 661 | 0.3296 | 0.3283 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 535 | -0.0348 | -0.0624 |
| seed_p | 535 | -0.3134 | -0.0788 |
| seed_p_vs_seed_pars | 378 | -0.6025 | -0.3503 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
