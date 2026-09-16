# YNL153C
Status: ok. Length: 602 nt. Measured usable bases: 299. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 299 | 0.3854 | 0.3643 |
| rnafold | ok | 299 | 0.3515 | 0.3430 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 128 | -0.0500 | -0.1594 |
| seed_p | 128 | -0.1193 | -0.3478 |
| seed_p_vs_seed_pars | 103 | -0.1431 | -0.4802 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
