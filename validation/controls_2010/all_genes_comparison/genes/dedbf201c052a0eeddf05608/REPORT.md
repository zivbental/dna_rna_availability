# YPL144W
Status: ok. Length: 553 nt. Measured usable bases: 283. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 283 | 0.3246 | 0.2985 |
| rnafold | ok | 283 | 0.3521 | 0.3073 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 88 | -0.2703 | -0.4367 |
| seed_p | 88 | 0.2360 | 0.1553 |
| seed_p_vs_seed_pars | 61 | -0.4696 | -0.2522 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
