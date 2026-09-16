# YOR230W
Status: ok. Length: 1541 nt. Measured usable bases: 1334. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 1334 | 0.3649 | 0.3407 |
| rnafold | ok | 1334 | 0.2984 | 0.2722 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 1289 | -0.1572 | -0.2250 |
| seed_p | 1289 | -0.3790 | -0.3646 |
| seed_p_vs_seed_pars | 1154 | -0.4485 | -0.4602 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
