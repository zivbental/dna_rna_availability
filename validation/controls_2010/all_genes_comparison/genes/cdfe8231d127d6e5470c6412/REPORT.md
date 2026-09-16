# YHR089C
Status: ok. Length: 841 nt. Measured usable bases: 620. Mapping: contiguous.
| Model | Status | Matched bases | Pearson r | Spearman rho |
| --- | --- | --- | --- | --- |
| rnaplfold | ok | 620 | 0.3271 | 0.3395 |
| rnafold | ok | 620 | 0.3261 | 0.3445 |

Positive per-base PARS/pairing correlation is the expected direction. Null correlations mean insufficient pairs or a constant signal, not zero correlation.

| Exploratory local-window comparison | Windows | Pearson r | Spearman rho |
| --- | --- | --- | --- |
| full_p | 465 | -0.2484 | 0.1025 |
| seed_p | 465 | -0.2025 | 0.0438 |
| seed_p_vs_seed_pars | 428 | -0.3766 | -0.2126 |

Negative PARS/opening-probability correlation is the expected tendency for the window diagnostics, but PARS does not measure joint opening or binding. Overlapping windows and selected best seeds are not independent observations. Full settings, warnings and status details: [checkpoint](result.json).
