# YAL044C
Status: ok. Length: 581 nt. Measured usable bases: 474. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 474 | 0.3946 | 0.3605 |
| rnafold | ok | 474 | 0.3561 | 0.3151 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 457 | -0.0370 | -0.0946 |
| seed_p | 457 | -0.4148 | -0.3018 |
| seed_p_vs_seed_pars | 423 | -0.4455 | -0.2620 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
